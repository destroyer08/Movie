
package hello;

//import java.util.ArrayList;
import java.util.List;

import hello.wsdl.ArrayOfString;
import hello.wsdl.ArrayOfVectorDetail;
//import hello.wsdl.EvaluateVectorCollection;
import hello.wsdl.EvaluateVectorCollectionCompressed;
import hello.wsdl.EvaluateVectorCollectionCompressedResponse;
//import hello.wsdl.GetVersion;
//import hello.wsdl.GetVersionResponse;
//import hello.wsdl.ObjectFactory;
//import hello.wsdl.VectorDetail;

//import org.neo4j.cypher.internal.compiler.v2_1.planner.logical.steps.verifyBestPlan;
import org.springframework.ws.client.core.support.WebServiceGatewaySupport;
import org.springframework.ws.soap.client.SoapFaultClientException;
import org.springframework.ws.soap.client.core.SoapActionCallback;
//import org.springframework.ws.soap.server.endpoint.annotation.SoapAction;

public class WebClient extends WebServiceGatewaySupport 
{
	
	
	public  ArrayOfVectorDetail getEvaluateVectorCollectionCompressedResponse(String SurveyCode, String TableCode, List<String> StrsProcess ) 
	{
	 
		EvaluateVectorCollectionCompressed request = new EvaluateVectorCollectionCompressed();
		
		ArrayOfString ar = new ArrayOfString();
		 
		ar.setString(StrsProcess);
		
		
		request.setSurveyCode(SurveyCode);
		request.setStrsProcess(ar);
		request.setTableCode(TableCode);
		try
			{
			EvaluateVectorCollectionCompressedResponse response = (EvaluateVectorCollectionCompressedResponse) getWebServiceTemplate().marshalSendAndReceive(
				
			request,
				new SoapActionCallback("net.Telmar/EvaluateVectorCollectionCompressed"));
			 ArrayOfVectorDetail arr = response.getEvaluateVectorCollectionCompressedResult();
		
			 return(arr);
			}
		catch(SoapFaultClientException e)
			{
			System.out.println("Exception:"+e);
			}
		return null;
	}

	
}
