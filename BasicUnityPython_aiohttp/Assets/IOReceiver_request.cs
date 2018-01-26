using System.Collections;
using System.Collections.Generic;
using UnityEngine;


//Create an interface class that the sdsim will expect. We can use this to wrap other car implementations
//like the Unity standard asset car.
public interface IOReceiver_request
{
	//all inputs require 0-1 input except steering which is in degrees, where 0 is center.
	void RequestBlendshapes(JSONObject jsonObject);
}
