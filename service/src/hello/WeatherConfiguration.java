
package hello;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;

@Configuration
public class WeatherConfiguration {

	@Bean
	public Jaxb2Marshaller marshaller() {
		Jaxb2Marshaller marshaller = new Jaxb2Marshaller();
		marshaller.setContextPath("hello.wsdl");
		return marshaller;
	}

	@Bean
	public WebClient weatherClient(Jaxb2Marshaller marshaller) {
		WebClient client = new WebClient();
		client.setDefaultUri("http://192.168.208.53:88//TNTEngineServiceMulti/TNTService.asmx");
		//client.setDefaultUri("http://172.16.0.15/TNTEngineServiceMulti/TNTService.asmx");
		client.setMarshaller(marshaller);
		client.setUnmarshaller(marshaller);
		return client;
	}

}
