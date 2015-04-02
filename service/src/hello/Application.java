
package hello;

import java.io.FileWriter;
import java.io.IOException;
//import java.util.StringTokenizer;

import javax.xml.parsers.ParserConfigurationException;

import hello.wsdl.ArrayOfVectorDetail;
/*import hello.wsdl.EvaluateVectorCollectionCompressedResponse;
import hello.wsdl.GetVersion;
import hello.wsdl.GetVersionResponse;
import hello.wsdl.VectorDetail;

import org.neo4j.cypher.internal.compiler.v2_1.ast.Null;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ApplicationContext;*/
import org.xml.sax.SAXException;

public class Application 
{

	public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException 
	{
		FileWriter fw = new FileWriter("out.csv");
		intermediate iobj = new intermediate();
		String pryName = "Second.pry";
		
		ArrayOfVectorDetail vec = iobj.getVector(args,pryName);
		//int[][] data = new int[vec.getVectorDetail().get(0).getDataLength()+1][vec.getVectorDetail().size()+1];
		//int[][] data = new int[vec.getVectorDetail().size()+1][vec.getVectorDetail().get(0).getDataLength()+1];
		for(int i=0;i<vec.getVectorDetail().size();i++)
			{
			String s = vec.getVectorDetail().get(i).getVectorData();
			
			//String[] ss = s.split(":");
			
			//for(int j=0;j<ss.length;j++)
			//	{
			//	data[j][i] = Integer.parseInt(ss[j],10);
				//System.out.println(ss[j]);
			//	}
			fw.write(s+"\n");
			}
	//	String[] fdata = new String[vec.getVectorDetail().get(0).getDataLength()+1];
	//	for(int i=0;i<vec.getVectorDetail().get(0).getDataLength();i++)
	//		{
	//		String temp2 = "";
	//		for(int j=0;j<vec.getVectorDetail().size();j++)
	//			{
	//			if (j == vec.getVectorDetail().size() - 1)
     //           	{
      //              temp2 += data[i][j];
      //              continue;
      //          	}
      //          	temp2 += (data[i][j] + ",");
		//		}
		//	fw.write(temp2+"\n");
		//	}
		fw.close();
		
	
		//System.out.println(vec.getVectorDetail().size());
	}

}
