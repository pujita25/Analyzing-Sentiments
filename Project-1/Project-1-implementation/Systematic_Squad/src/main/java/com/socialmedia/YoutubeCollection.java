package com.socialmedia;

import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.services.youtube.YouTube;
import com.google.api.services.youtube.model.CommentThreadListResponse;
import com.mongodb.DB;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.mongodb.DBCollection;
import com.google.api.client.googleapis.json.GoogleJsonResponseException;
import com.mongodb.DBObject;
import com.mongodb.util.JSON;
import java.io.IOException;
import java.security.GeneralSecurityException;

public class YoutubeCollection {
    private static final String SECRET_KEY = "AIzaSyAGDpCLDzAdlKfeZrxdX1PrYMHy1R7cu00";
    private static final String Appl_Name = "Youtube code samples";
    private static final JsonFactory JSON_FACTORY = JacksonFactory.getDefaultInstance();
    public static YouTube getService() throws GeneralSecurityException, IOException {
        final NetHttpTransport httpTransport = GoogleNetHttpTransport.newTrustedTransport();
        return new YouTube.Builder(httpTransport, JSON_FACTORY, null)
            .setApplicationName(Appl_Name)
            .build();
    }
    @SuppressWarnings("deprecation")
	public static void main(String[] args)
        throws GeneralSecurityException, IOException, GoogleJsonResponseException {
        YouTube youtubeService = getService();
        // Define and execute the API request
        YouTube.CommentThreads.List request = youtubeService.commentThreads()
            .list("snippet");
        request.setMaxResults((long) 100);
        CommentThreadListResponse response = request.setKey(SECRET_KEY)
            .setVideoId("Jo0D_u-QSXs")
            .execute();
        int count=0;
        com.mongodb.MongoClient mongoClient= new com.mongodb.MongoClient("localhost", 27017);				
        DB db = mongoClient.getDB("youtubedatabase");
        DBCollection collection = db.getCollection("youtube");
        
        DBObject db_obj;
        while(count<10) {
        	count= count+response.getItems().size();
        	for(int j=0;j<response.getItems().size();j++) {
        		System.out.println(response.toString());
            	db_obj = (DBObject)JSON.parse(response.getItems().get(j).getSnippet().getTopLevelComment().getSnippet().toString());
            	if(db_obj!=null) {
					collection.insert(db_obj);
				} else {
					break;
				}
            }
        	request.setPageToken(response.getNextPageToken());
        	response = request.setKey(SECRET_KEY)
                    .setVideoId("Jo0D_u-QSXs")
                    .execute();
        }
        mongoClient.close();
    }
}