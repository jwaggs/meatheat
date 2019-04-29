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
    
    let baseURL = URL.init(string: "https://meatheat.herokuapp.com/")!
    let devicesURL = "https://meatheat.herokuapp.com/devices/"
    
    public init() {
        NotificationCenter.default.addObserver(self, selector: #selector(onDidReceiveDeviceToken(_:)), name: .didReceiveFCMToken, object: nil)
    }
    
    @objc func onDidReceiveDeviceToken(_ notification:Notification) {
        guard let deviceRegistrationToken = notification.userInfo?["token"] as? String else{
            print("registration token not found in notification about itself")
            return
        }
        
        let url = "https://meatheat.herokuapp.com/devices/\(deviceRegistrationToken)/"
        print(url)
        
        Alamofire.request(url, method: .post).responseData { (responseData) in
            print(responseData)
        }
    }
}
