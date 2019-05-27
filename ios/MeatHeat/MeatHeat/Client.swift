//
//  Client.swift
//  MeatHeat
//
//  Created by Jonathan Waggoner on 4/29/19.
//  Copyright © 2019 meatheat. All rights reserved.
//

import Foundation
import Alamofire
import FirebaseMessaging

class MeatHeatClient {
    
    static let shared = MeatHeatClient()
    private init() {
        NotificationCenter.default.addObserver(self, selector: #selector(onDidReceiveDeviceToken(_:)), name: .didReceiveFCMToken, object: nil)
    }
    
    @objc func onDidReceiveDeviceToken(_ notification:Notification) {
        guard let deviceRegistrationToken = notification.userInfo?["token"] as? String else{
            print("registration token not found in notification about itself")
            return
        }
        
        //let url = "https://meatheat.herokuapp.com/devices/\(deviceRegistrationToken)/"
        let url = "https://meatheat.herokuapp.com/pair/device/\(deviceRegistrationToken)/controller/1/"
        Alamofire.request(url, method: .post).responseData { (responseData) in
            if responseData.response?.statusCode != 200 {
                print("error with code: \(responseData.response?.statusCode ?? -1) registering device token with server.")
            }
        }
    }
    
    public func threshold(low: Int?, high: Int?) {
        guard let fcmToken = Messaging.messaging().fcmToken else {
            print("No fcmToken found to set threshold with")
            return
        }
        
        var payload: [String:Any] = [:]
        payload["device"] = fcmToken
        payload["controller"] = 1  // TODO: put dynamic value
        payload["probe"] = 1  // TODO: put dynamic value
        payload["low"] = low
        payload["high"] = high
        
        let url = URL.init(string: "https://meatheat.herokuapp.com/threshold/")
        var request = URLRequest(url: url!)
        request.httpMethod = HTTPMethod.post.rawValue
        request.setValue("application/json; charset=UTF-8", forHTTPHeaderField: "Content-Type")
        do {
            let jsonData = try JSONSerialization.data(withJSONObject: payload, options: .prettyPrinted)
            request.httpBody = jsonData
            Alamofire.request(request).responseData { (responseData) in
                if responseData.response?.statusCode != 200 {
                    print("error with code: \(responseData.response?.statusCode ?? -1) sending threshold to server.")
                }
            }
        } catch {
            print("error encoding json for threshold")
            return
        }
        
//        guard let data = try? JSONEncoder().encode(payload) else {
//            print("ERROR ENCODING DATA")
//            return
//        }
        
        
        
    }
}
