//
//  ViewController.swift
//  MeatHeat
//
//  Created by Jonathan Waggoner on 4/29/19.
//  Copyright © 2019 meatheat. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var ProbeHigh: UITextField!
    @IBOutlet weak var ProbeLow: UITextField!
    @IBOutlet weak var LabelProbeCurrent: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(self, selector: #selector(onDidReceiveData(_:)), name: .didReceiveData, object: nil)
        
        //Looks for single or multiple taps to dismiss number pad
        let tap: UITapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(dismissKeyboard))
        //Uncomment the line below if you want the tap not not interfere and cancel other interactions.
        //tap.cancelsTouchesInView = false
        view.addGestureRecognizer(tap)
    }
    
    //Calls this function when the tap is recognized.
    @objc func dismissKeyboard() {
        //Causes the view (or one of its embedded text fields) to resign the first responder status.
        view.endEditing(true)
        threshold()
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
            if let payload = try JSONSerialization.jsonObject(with: jsonData, options : .allowFragments) as? Dictionary<String,Any> {
                handle(payload)
            } else {
                print("error: bad json")
            }
        } catch let error as NSError {
            print("error serializing json data to array: \(error)")
        }
        
    }
    
    func handle(_ payload: Dictionary<String,Any>) {
        let _ = payload["temp"] as? Double
        let tempDisplay = String(describing: payload["temp"]!)
        DispatchQueue.main.async {
            self.LabelProbeCurrent.text = tempDisplay
        }
    }
    
    func threshold() {
        let low = Int(self.ProbeLow.text!)
        let high = Int(self.ProbeHigh.text!)
        MeatHeatClient.shared.threshold(low: low, high: high)
    }
}

