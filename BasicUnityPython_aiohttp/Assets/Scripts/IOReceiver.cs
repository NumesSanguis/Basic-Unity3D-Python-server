using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IOReceiver : MonoBehaviour, IOReceiver_request {

    int blendShapeCount;
    //SkinnedMeshRenderer skinnedMeshRenderer;
    //Mesh skinnedMesh;
	//float blendVal = 0f;
	//Dictionary<string, int> blendDict = new Dictionary<string, int>();
	JSONObject blendJson;

	/*
    void Awake()
    {
        skinnedMeshRenderer = GetComponent<SkinnedMeshRenderer>();
        skinnedMesh = GetComponent<SkinnedMeshRenderer>().sharedMesh;
    }
    */

	/*
    void Start()
    {
		// Add all blendshapes of an object to a dict
        blendShapeCount = skinnedMesh.blendShapeCount;
		for (int i = 0; i < blendShapeCount; i++) {
			string expression = skinnedMesh.GetBlendShapeName(i);
			//Debug.Log(expression);
			blendDict.Add(expression, i);
		}

		Debug.Log(blendDict);
    }
	*/

	public void RequestBlendshapes(JSONObject blendJson)
	{
		Debug.Log(blendJson);

		/*
		// change blendshapes of an object based on data received from Python
		Debug.Log("Changing blendshapes");
		Debug.Log (blendJson);
		//Debug.Log (blendJson[3]);
		foreach (string key in blendJson.keys) {
			Debug.Log(key);
			blendVal = float.Parse(blendJson[key].ToString());
			Debug.Log(blendVal);
			Debug.Log(blendDict[key]);
			skinnedMeshRenderer.SetBlendShapeWeight(blendDict[key], blendVal*100);
		}
		*/


		//Debug.Log (jsonObject["data_stuff"]);
		//blendVal = float.Parse(jsonObject ["data_stuff"].ToString());  // works better
		//blendVal = float.Parse(jsonObject.GetField ("Expressions_browOutVertR_min").str);  // works worse

		//blendJson = jsonObject.GetField("data_stuff");
		//Debug.Log(blendJson);

		// not working if remember correctly
		// set blendshapes of face based on json
		// foreach (JSONObject o in blendJson) {
			// skinnedMeshRenderer.SetBlendShapeWeight(o[0].str, o[1].f*100);
		// }
	}

	/*
    void Update()
    {
		
    } */
}
