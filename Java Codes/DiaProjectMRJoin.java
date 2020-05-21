//Author: Richard Saldanha
// Student id : 18183034
// Course: Master of Science in Data Analytics
// Batch: A
// Subject: Data Intensive Architecture
// Code: Hadoop MapReduce using Reduce Side Join

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class DiaProjectMRJoin 
{
        public static class ParttimeMapper extends Mapper < Object, Text, Text, Text > 
        {
                public void map(Object key, Text value, Context context)
                throws IOException,InterruptedException
                {
                
                        String record = value.toString(); //Read each record
                        String[] parts = record.split(","); // Parse csv file
                        //System.out.println("Parttime"+parts);
                        context.write(new Text(parts[7]), new Text("PARTTIME@" + parts[6])); // Total percent of females and males in the country under observation who do part time.
                }
        }

   
        public static class TourismMapper extends Mapper < Object, Text, Text, Text >
        {
                public void map(Object key, Text value, Context context)
                throws IOException,InterruptedException
                {
                    String record = value.toString(); // Read each record
                    String[] parts = record.split(","); //Parse csv file

                    //System.out.println("Tourism"+parts[4]);
                    context.write(new Text(parts[5]), new Text("TOURISM@" + parts[4])); // Anual data on trips of EU residents in percent.            
                }      
        }  

        public static class DiaProjectReduceJoinReducer extends Reducer <Text, Text, Text, Text>
        {
                public void reduce(Text key, Iterable<Text> values, Context context)
                throws IOException, InterruptedException
                {
                double totalparttime=0.0;
                double totaltourism=0.0;

                for (Text t : values)
                {
                    String parts[] = t.toString().split("@");
                    if (parts[0].equals("PARTTIME")& parts[1] != null)
                     {
                        
                        totalparttime = Float.parseFloat(parts[1]);
                     }       
                    else if(parts[0].equals("TOURISM")& parts[1] != null)
                     {
                        totaltourism = Float.parseFloat(parts[1]);
                     }
                }   
                String str = String.format("%f  %f",totalparttime,totaltourism);
                context.write(new Text(key), new Text(str));
                }
         }

        public static void main(String[] args) throws Exception
        {
            Configuration conf = new Configuration();
            Job job = new Job(conf, "Reduce-side join");
            job.setJarByClass(DiaProjectMRJoin.class);
            job.setReducerClass(DiaProjectReduceJoinReducer.class);
            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(Text.class);

            MultipleInputs.addInputPath(job, new Path(args[0]),TextInputFormat.class, ParttimeMapper.class);
            MultipleInputs.addInputPath(job, new Path(args[1]), TextInputFormat.class, TourismMapper.class);
            Path outputPath = new Path(args[2]);

            FileOutputFormat.setOutputPath(job, outputPath);
            outputPath.getFileSystem(conf).delete(outputPath);
            System.exit(job.waitForCompletion(true) ? 0 : 1);
        
        }

}
