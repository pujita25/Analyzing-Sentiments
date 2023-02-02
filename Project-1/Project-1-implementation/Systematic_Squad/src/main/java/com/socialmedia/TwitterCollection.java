package com.socialmedia;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.config.CookieSpecs;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.HttpClients;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBObject;
import com.mongodb.util.JSON;

public class TwitterCollection {

	public static void main(String[] args) {

		// Authenticating using bearer token from the developer account
		String bearer_token = "AAAAAAAAAAAAAAAAAAAAADTciAEAAAAAOPqxEzXq%2BheAjelAA2GGJKQpRUo%3Dlx8ry4J3JlEu5dUEvhzwPlF1Esl6pGRyspFRhXb16pxUKzYFgo";
		if (bearer_token != null) {
			// System.out.println(bearer_token);
			try {
				// set up request
				HttpClient httpClient = HttpClients.custom()
						.setDefaultRequestConfig(RequestConfig.custom().setCookieSpec(CookieSpecs.STANDARD).build())
						.build();
				URIBuilder uri_builder = new URIBuilder("https://api.twitter.com/2/tweets/sample/stream#lang=en");

				// Authorization
				HttpGet http_get_req = new HttpGet(uri_builder.build());
				http_get_req.setHeader("Authorization", String.format("Bearer %s", bearer_token));
				http_get_req.setHeader("Content-Type", "application/json");

				// final_resp
				HttpResponse final_resp = httpClient.execute(http_get_req);

				// push the data from final_resp to mongodb
				if (final_resp.getEntity() != null) {
					BufferedReader br = new BufferedReader(new InputStreamReader((final_resp.getEntity().getContent())));
					String sent = br.readLine();

					com.mongodb.MongoClient mongo_db_client = new com.mongodb.MongoClient("localhost", 27017);
					DB db = mongo_db_client.getDB("twitterdatabase");
					DBCollection collection = db.getCollection("twitter");

					DBObject db_obj_collec;

					while (sent != null) {
						System.out.println("Fetching--------------");
						db_obj_collec = (DBObject) JSON.parse(sent);
						if (db_obj_collec != null) {
							collection.insert(db_obj_collec);
						}
						else {
							break;
						}
						sent = br.readLine();
					}
					br.close();
					mongo_db_client.close();
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		} else
			System.out.println("Verify the bearer token - Authentication error");
	}
}
