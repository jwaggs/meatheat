//
//  Client.swift
//  MeatHeat
//
//  Created by Jonathan Waggoner on 4/29/19.
//  Copyright © 2019 meatheat. All rights reserved.
//

import Foundation
import Alamofire

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
        
        let url = "https://meatheat.herokuapp.com/devices/\(deviceRegistrationToken)/"
        Alamofire.request(url, method: .post).responseData { (responseData) in
            if responseData.response?.statusCode != 200 {
                print("error with code: \(responseData.response?.statusCode ?? -1) registering device token with server.")
            }
        }
    }
    
    public func threshold(low: Int?, high: Int?) {
        var payload: [String:Int?] = [:]
        payload["low"] = low
        payload["high"] = high
        
        let url = "https://meatheat.herokuapp.com/threshold/"
        Alamofire.request(url, method: .post).responseData { (responseData) in
            if responseData.response?.statusCode != 200 {
                print("error with code: \(responseData.response?.statusCode ?? -1) sending threshold to server.")
            }
        }
    }
}
