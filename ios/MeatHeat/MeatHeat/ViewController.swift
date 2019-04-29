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
        guard let data = notification.userInfo?["data"] as? String else{
            print("registration token not found in notification about itself")
            return
        }
        
        
    }
}

