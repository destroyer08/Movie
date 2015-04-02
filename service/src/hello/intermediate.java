package hello;

import java.io.IOException;




import java.util.ArrayList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.springframework.boot.SpringApplication;
import org.springframework.context.ApplicationContext;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import hello.wsdl.ArrayOfVectorDetail;

public class intermediate 
{
	

	public ArrayOfVectorDetail getVector(String[] args,String pry_name) throws ParserConfigurationException, SAXException, IOException
	{
		ApplicationContext ctx = SpringApplication.run(WeatherConfiguration.class, args);

		WebClient webClient = ctx.getBean(WebClient.class);
		DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
		DocumentBuilder db = dbf.newDocumentBuilder();
		java.util.List<String> rowCode = new ArrayList<String>();
		Document dom = db.parse(pry_name);
		Element docEle = dom.getDocumentElement();
		NodeList nl = docEle.getElementsByTagName("Survey");
		String surCode = nl.item(0).getAttributes().item(0).getNodeValue();
		//System.out.println(surCode);
		nl = docEle.getElementsByTagName("CodeItem");
		
		String tabCode = nl.item(0).getAttributes().item(0).getNodeValue();
		nl = docEle.getElementsByTagName("CodeSet");
		
		//System.out.println(nl.item(2).getAttributes().item(0).getNodeValue());
		
		for(int i=0;i<nl.getLength();i++)
			{
			if(nl.item(i).getAttributes().item(0).getNodeValue().toString().equals("Rows"))
			 	{
				//System.out.println(nl.item(i).getChildNodes().getLength());
				for(int j=1;j<nl.item(i).getChildNodes().getLength();j+=2){
				rowCode.add(nl.item(2).getChildNodes().item(j).getAttributes().item(0).getNodeValue());
				 //System.out.println(nl.item(2).getChildNodes().item(j).getAttributes().item(0).getNodeValue());
			 	}
			 	}
			}
		//System.out.println(tabCode);
		//return null;
		return(webClient.getEvaluateVectorCollectionCompressedResponse(surCode,tabCode,rowCode));
	}
	
	

}
