//
//  Notifications.swift
//  MeatHeat
//
//  Created by Jonathan Waggoner on 4/29/19.
//  Copyright © 2019 meatheat. All rights reserved.
//

import Foundation

extension Notification.Name {
    static let didReceiveData = Notification.Name("didReceiveData")
    static let didReceiveFCMToken = Notification.Name("didReceiveFCMToken")
}
