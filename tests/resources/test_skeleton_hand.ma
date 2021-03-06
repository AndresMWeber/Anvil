//Maya ASCII 2018 scene
//Name: test_skeleton_hand.ma
//Last modified: Mon, Mar 12, 2018 01:21:27 PM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "7AB44A6D-47ED-C6D8-F74F-87A59C9C5B96";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -29.249758894571769 66.242807798463971 3.6844959664706511 ;
	setAttr ".r" -type "double3" -28.538352729621078 25.000000000001165 8.7733845139491479e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "D660578D-4717-E331-13E1-76AFA7DF7159";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 16.249183557566653;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -40.940672164925743 59.195222034049543 -7.0117549020067322 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "06B075ED-4A54-97BD-56C7-A4BB02C00A1B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "4B20E394-4514-2762-49A3-56B79F2646BB";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "77E6EDBB-48EA-58F5-E391-2DB317C79D4C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9CA68B22-429B-6E03-2BB1-6E866202B10F";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "C318F1E1-4CA3-49CE-71EA-61A709EBD944";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "DED20398-4EC4-EB27-0450-37AF17C60B0E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode joint -n "j_hand_r";
	rename -uid "54E4BB06-4D41-B92A-CAB2-20B9B267FD0A";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" -35.471969593529593 59.827886628249189 -7.0486469863760224 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 163.23793383733616 5.7934805250913755 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_pCup_r" -p "j_hand_r";
	rename -uid "511082BB-4108-D3CF-463A-4F934CD75005";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 3.0466599609285083 7.1054273576010019e-15 6.6613381477509392e-16 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 1.7216363033728386 -14.308030256116306 5.1232927808024096 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_pknuckle_r" -p "j_pCup_r";
	rename -uid "23F8FBBF-4516-16B4-EC20-088D5A469527";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.2460407984830724 -7.1054273576010019e-15 3.5527136788005009e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -5.2347823149428114 4.9837218628044226 -9.1945855617045869 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_pa_r" -p "j_pknuckle_r";
	rename -uid "46B2CAE4-4D8E-4766-710F-A794F8DADC56";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.7551601329870614 -1.4210854715202004e-14 -1.7763568394002505e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.67037057514618004 12.225179384276471 1.510066823768802 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_pb_r" -p "j_pa_r";
	rename -uid "8C38D22C-4AD2-1B1B-5510-369BEDC3A26C";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.1961305634666815 2.8421709430404007e-14 -1.6875389974302379e-14 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.22640100588152365 0.033511447691781444 -0.95358234910979911 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_pc_r" -p "j_pb_r";
	rename -uid "6AB0B3F2-4948-3FBA-BEEB-3B9CADD320D2";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.2916550269013669 -1.4210854715202004e-14 -4.4408920985006262e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -1.2019626687804845 0.19862489088476581 -5.0870981797581303 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_pend_r" -p "j_pc_r";
	rename -uid "C85C7F18-4AAE-B4CA-FC05-BEAD050075F7";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.1480987339115281 0 -9.3258734068513149e-15 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.5;
	setAttr -k on ".liw" yes;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_rCup_r" -p "j_hand_r";
	rename -uid "091AA753-4106-E7C8-DD8D-D985B2FE955C";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 3.0466599609285083 7.1054273576010019e-15 6.6613381477509392e-16 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 1.996500267807197 33.319335890749485 6.6458866365535396 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_rknuckle_r" -p "j_rCup_r";
	rename -uid "C008F3C8-4527-B204-F0AC-88A0BA16789B";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.1148830871962048 7.1054273576010019e-15 0 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 1.9019747460628902 -26.072748729416251 -6.5582801930590833 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_ra_r" -p "j_rknuckle_r";
	rename -uid "1A6744A1-4572-A88F-7986-7DB717E7AFB6";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.8378895283041743 -2.8421709430404007e-14 -9.7699626167013776e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.071631362292018622 9.5162420241118468 0.43326227840500164 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_rb_r" -p "j_ra_r";
	rename -uid "F60DF234-4649-0CC6-86C8-2BA2CEA4A76F";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.8116562101235871 7.1054273576010019e-15 6.2172489379008766e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -3.8239794700317691 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_rc_r" -p "j_rb_r";
	rename -uid "57F04820-4877-1B61-B0AF-2CA4844F7CB4";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.2916550269013456 1.4210854715202004e-14 -1.7763568394002505e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -5.0909641538742472 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_rend_r" -p "j_rc_r";
	rename -uid "358B18B6-4484-4781-B764-0C8C5BB263D6";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.148098733911521 0 2.6645352591003757e-15 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.5;
	setAttr -k on ".liw" yes;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_iknuckle_r" -p "j_hand_r";
	rename -uid "8C9D9416-4CDF-C73A-793F-FDA8A0B2C1D4";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 3.300365543592946 -0.59003166787442751 -2.2805525588194344 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.45016291243338991 37.738807605107283 -1.4575590954996376 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_ia_r" -p "j_iknuckle_r";
	rename -uid "271180FD-4918-28AE-F680-6686E729B0F7";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.6063110961608871 0 -1.0658141036401503e-14 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.50338253325933557 0.42490295693380914 -1.3090181639770779 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_ib_r" -p "j_ia_r";
	rename -uid "CF4C0CBD-4E1B-CAB7-B841-45863D1FE92B";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.2534872327372888 0 -7.1054273576010019e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.52657968282700374 -0.072731664952322819 -1.344472245817343 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_ic_r" -p "j_ib_r";
	rename -uid "4DB23809-499A-1F29-4791-309FEF94EF07";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.2910134582623662 0 7.1054273576010019e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 1.9779232274534797 -0.3216378805393918 -5.0871675038824034 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_iend_r" -p "j_ic_r";
	rename -uid "EC3C4443-48FE-570C-FD1A-75A175EA386E";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.1472401179151746 0 3.5527136788005009e-15 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.5;
	setAttr -k on ".liw" yes;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_mknuckle_r" -p "j_hand_r";
	rename -uid "1210BC3F-4C18-6074-D880-EA9941B621DD";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 3.7482765300376144 -0.57177709475850946 -1.4172904612478938 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 2.5141443052146526 23.943942600534466 8.6762192642392044 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_ma_r" -p "j_mknuckle_r";
	rename -uid "A84054D5-4826-6BC1-3E74-66AA2940A182";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 2.4005552680345659 -7.1054273576010019e-15 -8.8817841970012523e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.99449071433069391 0.36013346521340334 -7.7211419238777186 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_mb_r" -p "j_ma_r";
	rename -uid "105A2AFD-4DC3-9CD8-F966-06BBEB75F7D2";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.8116562101235729 0 7.1054273576010019e-15 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.5130668342477982 -0.049807730057781156 -3.8236555625736668 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_mc_r" -p "j_mb_r";
	rename -uid "58F1CF96-4137-AB4D-0AA3-C99D93B9FA45";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.2916550269013598 0 0 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.67641031442181954 -0.11164586022265367 -5.0897430212978856 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_mend_r" -p "j_mc_r";
	rename -uid "D52F939C-4C0B-CAEE-0225-6FBA186780BD";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.1480987339115387 0 -7.1054273576010019e-15 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.5;
	setAttr -k on ".liw" yes;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_ta_r" -p "j_hand_r";
	rename -uid "12AFA05E-4AC6-90EA-5174-9B9E10132261";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 0.49362148689236207 -0.41291527390909977 -0.78488577762870393 ;
	setAttr ".jo" -type "double3" -93.131221899747928 47.926343017731291 -9.3099766588270914 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_tb_r" -p "j_ta_r";
	rename -uid "922C6FBA-43F1-CFC4-6980-BEAB8FFEA95F";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.8301292719265092 0 -1.4210854715202004e-14 ;
	setAttr ".jo" -type "double3" 1.0799937801587638 1.7895222335017624 -0.21637377859577725 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_tc_r" -p "j_tb_r";
	rename -uid "0254EAB5-4D15-45CD-984B-50B579F2A28C";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.3021922643552344 5.3290705182007514e-15 -1.4210854715202004e-14 ;
	setAttr ".jo" -type "double3" 3.6384810215243144 6.2674211016196359 -0.88163709901719567 ;
	setAttr ".radi" 0.5;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode joint -n "j_tend_r" -p "j_tc_r";
	rename -uid "0AFFA9D1-4104-6E3F-F1AE-C79FF286968C";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	addAttr -is true -ci true -k true -sn "hubReleaseTag" -ln "hubReleaseTag" -dt "string";
	addAttr -ci true -h true -sn "fbxID" -ln "filmboxTypeID" -at "short";
	setAttr ".t" -type "double3" 1.1728377576470876 -7.1054273576010019e-15 2.8421709430404007e-14 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".radi" 0.5;
	setAttr -k on ".liw" yes;
	setAttr -l on -k on ".hubReleaseTag" -type "string" (
		"build.charHare.rigPuppet.hareB.v12&lf;build.charHare.rigPuppet.hareB.v13&lf;build.charHare.rigPuppet.hareB.v14&lf;build.charHare.rigPuppet.hareB.v15&lf;build.charHare.rigPuppet.hareB.v16&lf;build.charHare.rigPuppet.hareB.v17&lf;build.charHare.rigPuppet.hareB.v18&lf;build.charHare.rigPuppet.hareB.v19&lf;build.charHare.rigPuppet.hareB.v20&lf;build.charHare.rigPuppet.hareB.v21&lf;build.charHare.rigPuppet.hareB.v22&lf;build.charHare.rigPuppet.hareB.v23&lf;build.charHare.rigPuppet.hareB.v24&lf;build.charHare.rigPuppet.hareB.v25&lf;build.charHare.rigPuppet.hareB.v26&lf;build.charHare.rigPuppet.hareB.v27&lf;build.charHare.rigPuppet.hareB.v28&lf;build.charHare.rigPuppet.hareB.v29&lf;build.charHare.rigPuppet.hareB.v30&lf;build.charHare.rigPuppet.hareB.v31&lf;build.charHare.rigPuppet.hareB.v32&lf;build.charHare.rigPuppet.hareB.v33&lf;build.charHare.rigPuppet.hareB.v34&lf;build.charHare.rigPuppet.hareB.v35&lf;build.charHare.rigPuppet.hareB.v39&lf;build.charHare.rigPuppet.hareB.v40&lf;build.charHare.rigPuppet.hareB.v41&lf;build.charHare.rigPuppet.hareB.v42");
	setAttr ".fbxID" 5;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "8A33D9EE-42A2-6EED-129C-3DA9538A85D5";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "DAD71A0E-4BCA-F78A-44F9-FC85F3AADE3D";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "A9214943-4C4A-F980-9666-AFB5A6F55325";
createNode displayLayerManager -n "layerManager";
	rename -uid "6C83157D-4001-79F9-B7B4-F28B0892853C";
createNode displayLayer -n "defaultLayer";
	rename -uid "995BBD50-45A9-DD8E-54FD-50AE3DD46BA2";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "16DFBC1E-445B-128B-05C4-0D9FEDCF81B9";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "6213E8B1-4FFF-27BA-039D-80998687B4C3";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "B4551B7A-4B8C-BF9B-6269-BBBC2723B981";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 466\n            -height 676\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n"
		+ "            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n"
		+ "                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n"
		+ "                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n"
		+ "                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n"
		+ "                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n"
		+ "                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n"
		+ "                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n"
		+ "                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n"
		+ "                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n"
		+ "                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -highlightConnections 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n"
		+ "                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 466\\n    -height 676\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 466\\n    -height 676\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "8D70250B-4D60-536C-B1E7-A7A9D587FE85";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".etmr" no;
	setAttr ".tmr" 4096;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "j_hand_r.s" "j_pCup_r.is";
connectAttr "j_pCup_r.s" "j_pknuckle_r.is";
connectAttr "j_pknuckle_r.s" "j_pa_r.is";
connectAttr "j_pa_r.s" "j_pb_r.is";
connectAttr "j_pb_r.s" "j_pc_r.is";
connectAttr "j_pc_r.s" "j_pend_r.is";
connectAttr "j_hand_r.s" "j_rCup_r.is";
connectAttr "j_rCup_r.s" "j_rknuckle_r.is";
connectAttr "j_rknuckle_r.s" "j_ra_r.is";
connectAttr "j_ra_r.s" "j_rb_r.is";
connectAttr "j_rb_r.s" "j_rc_r.is";
connectAttr "j_rc_r.s" "j_rend_r.is";
connectAttr "j_hand_r.s" "j_iknuckle_r.is";
connectAttr "j_iknuckle_r.s" "j_ia_r.is";
connectAttr "j_ia_r.s" "j_ib_r.is";
connectAttr "j_ib_r.s" "j_ic_r.is";
connectAttr "j_ic_r.s" "j_iend_r.is";
connectAttr "j_hand_r.s" "j_mknuckle_r.is";
connectAttr "j_mknuckle_r.s" "j_ma_r.is";
connectAttr "j_ma_r.s" "j_mb_r.is";
connectAttr "j_mb_r.s" "j_mc_r.is";
connectAttr "j_mc_r.s" "j_mend_r.is";
connectAttr "j_hand_r.s" "j_ta_r.is";
connectAttr "j_ta_r.s" "j_tb_r.is";
connectAttr "j_tb_r.s" "j_tc_r.is";
connectAttr "j_tc_r.s" "j_tend_r.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of test_skeleton_hand.ma
