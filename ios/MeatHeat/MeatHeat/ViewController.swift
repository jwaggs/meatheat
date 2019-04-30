//
//  ViewController.swift
//  MeatHeat
//
//  Created by Jonathan Waggoner on 4/29/19.
//  Copyright © 2019 meatheat. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var LabelProbeLow: UIButton!
    @IBOutlet weak var LabelProbeCurrent: UILabel!
    @IBOutlet weak var LabelProbeHigh: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(self, selector: #selector(onDidReceiveData(_:)), name: .didReceiveData, object: nil)
    }

    @objc func onDidReceiveData(_ notification:Notification) {
        guard let jsonString = notification.userInfo?["payload"] as? String else{
            print("payload not found in notification about itself")
            return
        }
        
        print(jsonString)
        guard let jsonData = jsonString.data(using: .utf8) else {
            print("could not parse json string into data")
            return
        }
        
        do {
            if let payload = try JSONSerialization.jsonObject(with: jsonData, options : .allowFragments) as? [Dictionary<String,Any>] {
                handle(payload)
            } else {
                print("error: bad json")
            }
        } catch let error as NSError {
            print("error serializing json data to array: \(error)")
        }
        
    }
    
    func handle(_ payload: [Dictionary<String,Any>]) {
        guard let temp = payload[0]["temp"] as? Float else {
            print("warning: payload does not have temp")
            return
        }
        LabelProbeCurrent.text = String(temp)
    }
}

