//Maya ASCII 2017 scene
//Name: test_skeleton_externalA.ma
//Last modified: Wed, Dec 13, 2017 07:16:01 PM
//Codeset: 1252
requires maya "2017";
requires "stereoCamera" "10.0";
requires -dataType "ngSkinLayerDataStorage" "ngSkinTools" "1.7.3";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201606150345-997974";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode joint -n "Root_M";
	rename -uid "AEBC84F7-4284-700A-F04A-EAB9194DC4BB";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.64999999999999991 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -s 2 ".iog";
	setAttr ".t" -type "double3" -3.7303493627405222e-014 95.028739420738759 4.7457389038350142 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 -6.3611093629270335e-015 -3.1805546814635168e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 7.5917370072731778 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 3.3306690738754696e-016 0.9912346034879731 -0.13211343931652439 0
		 -2.7755575615628909e-016 0.13211343931652442 0.9912346034879731 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 2.0217433865749377e-015 95.028739420738745 4.7457389038350097 1;
createNode joint -n "Hip_R" -p "Root_M";
	rename -uid "D5729162-4510-00D7-B760-B28F99E6E5DE";
	addAttr -ci true -sn "fat" -ln "fat" -dv 8.9242159449525893 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.0547977341199726 -0.82778875555604259 -8.4081152751406698 ;
	setAttr ".r" -type "double3" 2.3854154286560307e-015 -2.733289687695275e-015 -2.4418523320299742e-005 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.5468898240919717 178.00388103746735 8.1269092863036292 ;
	setAttr ".bps" -type "matrix" -0.034831759833711 -0.99934959032840764 -0.0093351388490383169 0
		 -0.096601694743973426 -0.0059303647300032744 0.99530545228425304 0 -0.99471345677007861 0.03557003070863559 -0.096332299027417967 0
		 -8.4081152751406645 92.882590783986288 4.1966724407040035 1;
	setAttr -k on ".twistAmount";
	setAttr -k on ".twistAddition";
createNode joint -n "HipPart1_R" -p "Hip_R";
	rename -uid "3920805B-41C6-9D8B-B29F-B3BCA5B3EECE";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 12.092250823974609 -3.5527136788005009e-015 7.1054273576010019e-015 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.034831759833711 -0.99934959032840764 -0.0093351388490383169 0
		 -0.096601694743973426 -0.0059303647300032744 0.99530545228425304 0 -0.99471345677007861 0.03557003070863559 -0.096332299027417967 0
		 -8.8293096516903464 80.798204876898922 4.0837896002647947 1;
	setAttr -k on ".twistAmount" 0.33333333333333331;
	setAttr -k on ".twistAddition";
createNode joint -n "HipPart2_R" -p "HipPart1_R";
	rename -uid "879C1067-4245-A2BE-4696-12B19D0C1C8F";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 12.092250823974609 -7.1054273576010019e-015 1.7763568394002505e-015 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.034831759833711 -0.99934959032840764 -0.0093351388490383169 0
		 -0.096601694743973426 -0.0059303647300032744 0.99530545228425304 0 -0.99471345677007861 0.03557003070863559 -0.096332299027417967 0
		 -9.2505040282400266 68.713818969811527 3.9709067598255872 1;
	setAttr -k on ".twistAmount" 0.66666666666666663;
	setAttr -k on ".twistAddition";
createNode joint -n "Knee_R" -p "HipPart2_R";
	rename -uid "7188BED2-4C01-12EF-0018-E5B65AA95284";
	addAttr -ci true -sn "fat" -ln "fat" -dv 6.1546316861741994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 12.092250823974631 -5.3290705182007514e-015 0 ;
	setAttr ".r" -type "double3" 0 0 4.2915619003150615e-005 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -6.3511207478296496 ;
	setAttr ".bps" -type "matrix" -0.023931873837728261 -0.99256029794333622 -0.11937889411973618 0
		 -0.099861926354022454 -0.11644238000840948 0.98816434250727803 0 -0.99471345677007861 0.03557003070863559 -0.096332299027417967 0
		 -9.6716984047897139 56.629433062724154 3.858023919386377 1;
createNode joint -n "Ankle_R" -p "Knee_R";
	rename -uid "4A0A2CDE-4634-6DBE-8BB8-3B8CCE89AAA8";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.7953562064740889 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 47.881469726562507 4.7295500849031669e-014 -3.0730973321624333e-013 ;
	setAttr ".r" -type "double3" 2.3355227347271652e-014 2.040281636935769e-006 -1.5386880222895956e-005 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.2252878497277564 2.0384426397554036 6.6910983514862892 ;
	setAttr ".bps" -type "matrix" 1.2558736620094102e-009 -0.99999999999999889 5.2165333041913342e-008 0
		 0.012108284039574965 5.2176715439541943e-008 0.99992669204177886 0 -0.9999266920417802 -6.2414895474205423e-010 0.012108284039574979 0
		 -10.817591697450508 9.1041872049624217 -1.8580129853982079 1;
createNode joint -n "Toes_R" -p "Ankle_R";
	rename -uid "BC02019D-40CE-7CA6-1C59-8D94A1D1278B";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.0773158430870993 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.8328421399717936 13.770143360887303 -3.907985046680551e-014 ;
	setAttr ".r" -type "double3" -5.4665783587401508e-016 6.5598940305187142e-015 -4.4141354936031386e-011 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.050291826167511045 -0.69189029984925809 85.842518661492093 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 9.5622534504111178e-007 -0.072492741347817358 0.99736893998708631 0
		 6.824312471208089e-008 0.99736893998754483 0.072492741347785286 0 -0.99999999999954059 -1.2558236818096916e-009 9.5865658992361213e-007 0
		 -10.65085888178999 2.2713457834714799 11.911121270832378 1;
createNode joint -n "ToesEnd_R" -p "Toes_R";
	rename -uid "6B9BE613-40AE-0924-C108-9AA126879CF7";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.0773158430870993 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 11.371045390346557 -1.4117595981133491e-012 2.1429772328218633e-005 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.9341138710255281e-006 0 0 ;
	setAttr ".ssc" no;
createNode joint -n "RootPart1_M" -p "Root_M";
	rename -uid "686E14D6-4759-E09D-5043-29AE62F6000A";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.65 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.9986610476140783 -1.4210854715202004e-014 -3.381764456008176e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 3.3306690738754696e-016 0.9912346034879731 -0.13211343931652439 0
		 -2.7755575615628909e-016 0.13211343931652442 0.9912346034879731 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 9.7100132154925257e-016 101.96605442921719 3.8211217222241118 1;
createNode joint -n "RootPart2_M" -p "RootPart1_M";
	rename -uid "5025B688-462B-5C92-F1B6-08ABB0A325A0";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.65 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.9986610476142062 1.4210854715202004e-014 -3.7702681878386441e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 3.3306690738754696e-016 0.9912346034879731 -0.13211343931652439 0
		 -2.7755575615628909e-016 0.13211343931652442 0.9912346034879731 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -4.6824447530681747e-016 108.9033694376958 2.8965045406132179 1;
createNode joint -n "Spine1_M" -p "RootPart2_M";
	rename -uid "5E04B4ED-4370-3B53-6D89-9E8C35B28C9F";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.65 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.9986610476141493 0 -1.0922300831685407e-014 ;
	setAttr ".r" -type "double3" 0 0 3.1805546814635168e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 4.2465227074723062 ;
	setAttr ".bps" -type "matrix" 3.1160009305158782e-016 0.99829607978119805 -0.058351838818429327 0
		 -3.0145670432490962e-016 0.058351838818429355 0.99829607978119805 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -9.0595229160096848e-015 115.84068444617434 1.9718873590023267 1;
createNode joint -n "Spine1Part1_M" -p "Spine1_M";
	rename -uid "A5AA4E60-4324-814E-277D-8589CBEF97ED";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.65 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5488565216178785 -1.7763568394002505e-015 -3.4828957335286654e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 3.1160009305158782e-016 0.99829607978119805 -0.058351838818429327 0
		 -3.0145670432490962e-016 0.058351838818429355 0.99829607978119805 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -1.0790585933591296e-014 121.3800861589738 1.6481013776262898 1;
createNode joint -n "Spine1Part2_M" -p "Spine1Part1_M";
	rename -uid "7472522B-4F9D-8967-020B-65BA619A776A";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.64999999999999991 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5488565216179637 -5.3290705182007514e-015 -5.3310362147210886e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 3.1160009305158782e-016 0.99829607978119805 -0.058351838818429327 0
		 -3.0145670432490962e-016 0.058351838818429355 0.99829607978119805 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -1.4369789432365287e-014 126.91948787177336 1.3243153962502419 1;
createNode joint -n "Chest_M" -p "Spine1Part2_M";
	rename -uid "37E43920-46FC-BE55-1581-52B913BAB81D";
	addAttr -ci true -sn "fat" -ln "fat" -dv 17.438123110826901 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 0.64999999999999991 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5488565216177648 8.8817841970012523e-015 -1.1755411321384367e-014 ;
	setAttr ".r" -type "double3" 0 0 3.776908684237926e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -1.3334384327780588 ;
	setAttr ".bps" -type "matrix" 3.1853084700072364e-016 0.99666784630072558 -0.081567175691410448 0
		 -2.9412388900120938e-016 0.081567175691410476 0.99666784630072558 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -2.4373368037802654e-014 132.45888958457269 1.0005294148742241 1;
createNode joint -n "Scapula_R" -p "Chest_M";
	rename -uid "8D0B024E-481C-3F68-8F4D-899102EB5194";
	addAttr -ci true -sn "fat" -ln "fat" -dv 6.6675176600220505 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.1944024239794544 -1.4630365309524951 -8.4006089389264549 ;
	setAttr ".r" -type "double3" 1.8288189418415214e-014 2.0692241492099566e-014 3.1706154480839439e-014 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 16.40380352099946 106.38824287079173 13.304616761789939 ;
	setAttr ".bps" -type "matrix" -0.95937189098325348 -0.27895312508271031 -0.042317003648726439 0
		 -0.079679084802483369 0.12398856345646281 0.98907941014715373 0 -0.2706599679233247 0.95226676416778955 -0.14117787229290685 0
		 -8.4006089389264726 139.5099833961379 -1.0444591400009338 1;
createNode joint -n "Shoulder_R" -p "Scapula_R";
	rename -uid "746DFD6C-4776-826B-58EC-609CC0F58618";
	addAttr -ci true -sn "fat" -ln "fat" -dv 6.6675176600220505 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 11.285022620381564 -1.1368683772161603e-012 5.6843418860808015e-014 ;
	setAttr ".r" -type "double3" 1.6300342742500524e-014 -2.7145523733008474e-030 -1.9083328088781101e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.3132100613080168e-016 41.559621793263709 -10.207505970295202 ;
	setAttr ".bps" -type "matrix" -0.51638190166296782 -0.85360146643048396 -0.068660528272542931 0
		 -0.24843165013365801 0.072592015993870884 0.96592552219403216 0 -0.81953123604094857 0.5158439063531457 -0.24954682412629908 0
		 -19.227142430030646 136.36199106955326 -1.5220074834047166 1;
	setAttr -k on ".twistAmount";
	setAttr -k on ".twistAddition";
createNode joint -n "ShoulderPart1_R" -p "Shoulder_R";
	rename -uid "CCA99607-4C4C-830E-85F3-C89C5657B632";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.2660061136377436 1.7763568394002505e-015 7.1054273576010019e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.51638190166296782 -0.85360146643048396 -0.068660528272542931 0
		 -0.24843165013365801 0.072592015993870884 0.96592552219403216 0 -0.81953123604094857 0.5158439063531457 -0.24954682412629908 0
		 -22.97917634005676 130.15971783460651 -2.0208952823946862 1;
	setAttr -k on ".twistAmount" 0.33333333333333331;
	setAttr -k on ".twistAddition";
createNode joint -n "ShoulderPart2_R" -p "ShoulderPart1_R";
	rename -uid "B7C9FB50-4B65-70ED-577F-4494EDF98209";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.2660061136377152 -3.5527136788005009e-015 7.1054273576010019e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.51638190166296782 -0.85360146643048396 -0.068660528272542931 0
		 -0.24843165013365801 0.072592015993870884 0.96592552219403216 0 -0.81953123604094857 0.5158439063531457 -0.24954682412629908 0
		 -26.731210250082849 123.95744459965979 -2.5197830813846416 1;
	setAttr -k on ".twistAmount" 0.66666666666666663;
	setAttr -k on ".twistAddition";
createNode joint -n "Elbow_R" -p "ShoulderPart2_R";
	rename -uid "2A8AD9AA-4D60-3B16-7E2B-95865C6A1709";
	addAttr -ci true -sn "fat" -ln "fat" -dv 4.615973764630648 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.2660061136377294 0 5.6843418860808015e-014 ;
	setAttr ".r" -type "double3" 0 0 -2.2263882770244617e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 14.707844589729639 ;
	setAttr ".bps" -type "matrix" -0.56253596756210855 -0.80720123403731414 0.17882799827655535 0
		 -0.10918717118854915 0.28693419462825298 0.95170737603576372 0 -0.81953123604094857 0.5158439063531457 -0.24954682412629908 0
		 -30.483244160108992 117.75517136471304 -3.0186708803746134 1;
	setAttr -k on ".twistAmount";
	setAttr -k on ".twistAddition";
createNode joint -n "ElbowPart1_R" -p "Elbow_R";
	rename -uid "DECBC4BD-4FFE-3361-2A80-03BB6F641CC2";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.9778149385249151 -2.8421709430404007e-014 1.4210854715202004e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.56253596756210855 -0.80720123403731414 0.17882799827655535 0
		 -0.10918717118854915 0.28693419462825298 0.95170737603576372 0 -0.81953123604094857 0.5158439063531457 -0.24954682412629908 0
		 -34.408516068164396 112.12267049183313 -1.7708421937470598 1;
	setAttr -k on ".twistAmount" 0.33333333333333331;
	setAttr -k on ".twistAddition";
createNode joint -n "ElbowPart2_R" -p "ElbowPart1_R";
	rename -uid "1F29ECB4-4F3D-D5EC-683A-39AF5EF72E41";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.9778149385249151 -4.2632564145606011e-014 0 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.56253596756210855 -0.80720123403731414 0.17882799827655535 0
		 -0.10918715113290629 0.28693418200447396 0.9517073821426959 0 -0.81953123871298672 0.51584391337502511 -0.24954680083602968 0
		 -38.333787976219782 106.49016961895325 -0.52301350711951811 1;
	setAttr -k on ".twistAmount" 0.66666666666666663;
	setAttr -k on ".twistAddition";
createNode joint -n "Wrist_R" -p "ElbowPart2_R";
	rename -uid "F7317CF3-4D62-98E5-C390-94839761AF15";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.7438123110826886 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 2.3100000000000005 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.9778149385249151 -3.5527136788005009e-014 1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 1.9033631921883246e-014 -2.5692918286197465e-014 4.8304674224727165e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -13.521250444602606 8.3330281096852374 -4.339843371200649 ;
	setAttr ".bps" -type "matrix" -0.42805401778948904 -0.89263225613074271 0.14134147717218762 0
		 0.061070304255969515 0.12746699004446349 0.98996090043349094 0 -0.90168740469874542 0.43238850789994948 -4.9433753468469677e-005 0
		 -42.259059884275203 100.85766874607334 0.72481517950802621 1;
createNode joint -n "MiddleFinger1_R" -p "Wrist_R";
	rename -uid "A52FCB87-4118-A909-7686-7C82ACF42A5B";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 11.622556951389782 -1.7408297026122455e-013 1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 3.9160579515519545e-014 1.4610673067973045e-014 4.5148967626712571e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.2470179662951564 14.054891263265455 -7.7773719725676358 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.20046082362649045 -0.97968391885332096 0.0059057032763602593 0
		 -0.0016413236605683683 0.0063638860507450584 0.99997840327227794 0 -0.97970034410917206 0.20044680115814353 -0.0028836882350898531 0
		 -47.234142084304764 90.482999512546243 2.3675645475351681 1;
createNode joint -n "MiddleFinger2_R" -p "MiddleFinger1_R";
	rename -uid "EA73F796-45D6-4857-B3EC-A393922D48AA";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.019335210069201 0 2.8421709430404007e-014 ;
	setAttr ".r" -type "double3" 1.138381941852069e-014 2.5429573189874453e-014 -4.22615426796857e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.038232417324449618 7.0462296279878673 0.014371144227983391 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.078767258146574037 -0.99687207743178596 0.0064637667737890061 0
		 -0.0022562503577722025 0.0066621642623863712 0.99997526214485133 0 -0.99689047963073352 0.078750725737455327 -0.0027739533936289372 0
		 -48.039861330946209 86.545321442760468 2.3913015486540616 1;
createNode joint -n "MiddleFinger3_R" -p "MiddleFinger2_R";
	rename -uid "9391795F-457D-9DCB-FA56-ADA7412044F7";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.4939868148701549 -1.1501910535116622e-013 -4.9737991503207013e-014 ;
	setAttr ".r" -type "double3" 3.2726648767406716e-014 1.1175254154605861e-014 9.0627075296297561e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.052362469576962285 -1.8461493596731946 -0.0073031615319729768 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.11084171873893746 -0.99381845937888325 0.0062436515582412686 0
		 -0.0031745530398086348 0.0066363785637354707 0.99997293998015591 0 -0.99383300186701173 0.11081889855679478 -0.0038905170174459297 0
		 -48.315073092353764 83.062263548101626 2.413885864535962 1;
createNode joint -n "MiddleFinger4_R" -p "MiddleFinger3_R";
	rename -uid "F0CC5916-4C1C-CE3D-9F65-659011FDD8AA";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 2.7372071378116942 2.5757174171303632e-014 2.8421709430404007e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "ThumbFinger1_R" -p "Wrist_R";
	rename -uid "6DC0A681-4CD6-0696-E3D1-80B09C7CB5AE";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.6219143871222315 4.243363645569044 -2.0819457254230542 ;
	setAttr ".r" -type "double3" 8.3489560388417288e-015 -1.5902773407317584e-014 -1.6697912077683464e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -65.013753730819147 23.92261286006033 18.134507052022812 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011165504880348842 -0.91448913800131038 0.40445636103093646 0
		 0.97040915752422741 0.10748018126208281 0.21622691236057789 0 -0.24120820569351706 0.39007387391812098 0.88862870446133113 0
		 -42.529135178567415 95.480046008743003 5.720291877345451 1;
createNode joint -n "ThumbFinger2_R" -p "ThumbFinger1_R";
	rename -uid "C9E955AD-4F9E-B48C-3916-5B80E8BF1661";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.6060315911736893 3.1974423109204508e-014 -2.1316282072803006e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011165504880348842 -0.91448913800131038 0.40445636103093646 0
		 0.97040915752422741 0.10748018126208281 0.21622691236057789 0 -0.24120820569351706 0.39007387391812098 0.88862870446133113 0
		 -42.488872015237455 92.182369287325031 7.1787742924741407 1;
createNode joint -n "ThumbFinger3_R" -p "ThumbFinger2_R";
	rename -uid "709A2AC9-4497-CFC0-F9AE-F0A64F733961";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.6857353204954961 1.0658141036401503e-014 2.2737367544323206e-013 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011165504880348842 -0.91448913800131038 0.40445636103093646 0
		 0.97040915752422741 0.10748018126208281 0.21622691236057789 0 -0.24120820569351706 0.39007387391812098 0.88862870446133113 0
		 -42.447718919528839 88.811804371184238 8.6694933879251455 1;
createNode joint -n "ThumbFinger4_R" -p "ThumbFinger3_R";
	rename -uid "A4E33E89-4762-856B-38DA-46AB0276BC8D";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 3.2303742869033698 -3.7872524387694284e-006 -2.4202093271696867e-006 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "IndexFinger1_R" -p "Wrist_R";
	rename -uid "71E17120-4ED3-CD90-C727-0594D8DF4D0E";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 12.217774799299363 2.2419819373603662 -0.8777244184949069 ;
	setAttr ".r" -type "double3" 1.2722218725854067e-014 2.5183532575494324e-014 -9.8398410457777569e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.64306410152709848 21.375558310333062 5.5803899526520597 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.0625429166580736 -0.97334415359470272 0.22065706931551726 0
		 0.11354162686723107 0.21271545585491938 0.97049494270128811 0 -0.99156274765858554 0.085751346948287455 0.097211233673432165 0
		 -46.560575903558082 89.857949599706458 4.6712113640755355 1;
createNode joint -n "IndexFinger2_R" -p "IndexFinger1_R";
	rename -uid "5C820B41-4CB3-5910-77DA-2AA3A9ECCB2F";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.7112077937487413 -7.1054273576010019e-015 -1.0658141036401503e-013 ;
	setAttr ".r" -type "double3" 2.2227678336156908e-014 5.9580234895184563e-015 4.8865013369245834e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0012331905352439272 -2.482711773244052 0.028468356187128653 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.10538029191967682 -0.96861022871313573 0.22514266345410994 0
		 0.1135939516541763 0.21319630037306611 0.9703833014097194 0 -0.98792277442243048 0.12783412040423428 0.087561575122671723 0
		 -46.730142746645129 87.21901134448072 5.2694585301495023 1;
createNode joint -n "IndexFinger3_R" -p "IndexFinger2_R";
	rename -uid "84F49D9A-4EB7-BFF6-4D9E-C5B029A08D01";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.1608979938009441 9.5923269327613525e-014 4.2632564145606011e-014 ;
	setAttr ".r" -type "double3" 4.2443632541209924e-015 3.4703842798170945e-015 -2.0276036094329921e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.6269906615827949 7.0421664309703118 -0.081032153644932922 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.016374442466681557 -0.97727393722278955 0.21134694050061972 0
		 0.14160446881518185 0.2115113510400656 0.96706314312601982 0 -0.98978788234928183 0.014092551446538523 0.14184973721601007 0
		 -47.063239099960228 84.1573332157663 5.9811115233807062 1;
createNode joint -n "IndexFinger4_R" -p "IndexFinger3_R";
	rename -uid "D1DBAEDA-42D3-165B-9212-B4B3611BA68A";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 3.0498988820505275 -8.5975671026972122e-013 7.1054273576010019e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "Cup_R" -p "Wrist_R";
	rename -uid "B1230F5F-42E4-B950-37E1-689F6C52523D";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.23092633723484 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.9195468362663064 -1.3180287923802378 0.1026297234232203 ;
	setAttr ".r" -type "double3" -6.6924818507967983e-015 2.1376411475277925e-014 -3.4446846217309207e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.0014439751563087252 0.68668985185058207 0.12048458776555422 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.41708745257772384 -0.89748020134707762 0.14341319706440578 0
		 0.061947451063894286 0.12935440778526988 0.98966153329974826 0 -0.90675276134617389 0.42165948984521984 0.0016445104309037294 0
		 -43.25376196820131 99.020590072888808 -0.30867527862733879 1;
createNode joint -n "PinkyFinger1_R" -p "Cup_R";
	rename -uid "7A0F7480-4959-DA4C-4E08-D6B5C4840D77";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 8.4115546922500855 -3.1218164334996619 -0.024367626743824644 ;
	setAttr ".r" -type "double3" 2.4649298781342254e-014 1.9083328088781101e-014 -1.8884543421189673e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.8666739182807979 20.591376094394068 -29.127944866024979 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.050385210769664734 -0.94113378304355966 -0.33425818307083294 0
		 -0.11666099182542616 -0.32684610217709231 0.93784958201086255 0 -0.99189290930120277 0.086248640022667244 -0.093325390822841109 0
		 -46.933409044917354 91.057290717015022 -2.1919290390036368 1;
createNode joint -n "PinkyFinger2_R" -p "PinkyFinger1_R";
	rename -uid "B093B2D0-4A3F-B4EC-EACD-9691BDF42693";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.4499301332412671 -5.3290705182007514e-014 -4.9737991503207013e-014 ;
	setAttr ".r" -type "double3" 2.8427760470795739e-014 3.1791666830521116e-014 -8.7837974991980796e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.25314265926258378 20.082497249706876 -0.025671567371564948 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.2933163968933174 -0.91338989443454988 -0.28228423983347611 0
		 -0.12087466566247747 -0.32833421062618023 0.93679558140154973 0 -0.94834319026104996 -0.24065649145062526 -0.20671150574694477 0
		 -47.056849291051641 88.751578702525251 -3.0108382339913824 1;
createNode joint -n "PinkyFinger3_R" -p "PinkyFinger2_R";
	rename -uid "400BA545-4686-6E3C-2073-B6A4718C90C5";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.2517172873993303 -7.1054273576010019e-015 -2.8421709430404007e-014 ;
	setAttr ".r" -type "double3" 4.5785311513787611e-014 4.3259154405030008e-014 1.2945851476894453e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.1500272209346432 -3.7268268235112041 -0.16120539085996816 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.23139245678928988 -0.92617546234826864 -0.29775248762182849 0
		 -0.15618354190221545 -0.33745420029834916 0.92829486906902636 0 -0.96024175715279914 -0.16829639225180171 -0.22273772059337488 0
		 -46.39638368948922 86.69488288709114 -3.6464625367847909 1;
createNode joint -n "PinkyFinger4_R" -p "PinkyFinger3_R";
	rename -uid "41C5C1BC-4DB4-3C9F-8D49-FBB1CE2248A2";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 2.2660312317578217 -4.9737991503207013e-014 5.8975047068088315e-013 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "RingFinger1_R" -p "Cup_R";
	rename -uid "3E0CBAFE-4115-0C9D-C45D-ACBDD8915B2D";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 9.8257760639164786 -1.2976222365335897 -0.013665685612508582 ;
	setAttr ".r" -type "double3" 5.6653630263568892e-014 -1.2001624305834977e-014 2.5382317243085807e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.3131310013746243 6.09341515310396 -15.716307750779082 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.31965968223069596 -0.93864646959853437 -0.12946232141584052 0
		 -0.058516190648569923 -0.1168143263528179 0.99142839811592931 0 -0.94572381961551055 0.32449532857800145 -0.017585185324700398 0
		 -47.419962868131663 90.028535170694198 -0.18375860527638141 1;
createNode joint -n "RingFinger2_R" -p "RingFinger1_R";
	rename -uid "B926E851-4E63-3EDC-E544-D8966CD43B74";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.9819387449465182 8.8817841970012523e-016 -2.2737367544323206e-013 ;
	setAttr ".r" -type "double3" 3.015936128614331e-014 9.5576794106759895e-015 -2.7811217400219072e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.18148233733571445 24.27272342856552 0.19982687626795681 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.097182806533610333 -0.98942912274313488 -0.10763602176781509 0
		 -0.054253473528558548 -0.11325364361259832 0.9920837529254054 0 -0.99378672899387066 -0.090573855367988454 -0.064686273655559262 0
		 -48.373168459772451 87.229548895190916 -0.56980731751699509 1;
createNode joint -n "RingFinger3_R" -p "RingFinger2_R";
	rename -uid "317AEA88-4527-C832-223E-26951F16C9C1";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.7288466880779367 -2.3092638912203256e-014 4.9737991503207013e-014 ;
	setAttr ".r" -type "double3" 3.5066202593232411e-014 9.874689633515137e-015 -6.2378007488116994e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.48486173250853093 -1.1387291408775186 -0.0013569562278144185 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.077415111810130527 -0.99103103379770485 -0.10892378304703498 0
		 -0.062673666240139717 -0.11387293930888083 0.99151649772113015 0 -0.99502709110025978 -0.069931707708367263 -0.070927034574603282 0
		 -48.107971480025128 84.52954851050545 -0.86352951903600861 1;
createNode joint -n "RingFinger4_R" -p "RingFinger3_R";
	rename -uid "7BDEEC62-4487-C714-0D2C-75A99806F752";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 2.725646168215917 -8.8817841970012523e-014 -2.1316282072803006e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "Neck_M" -p "Chest_M";
	rename -uid "2FD95DA4-45D8-2D08-C80F-BCB3D6522BE3";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.28247023262624 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 18.152791037663519 5.2402526762307389e-013 2.2207502655616747e-014 ;
	setAttr ".r" -type "double3" 0 0 2.2263882770244617e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 28.112406580734238 ;
	setAttr ".bps" -type "matrix" 1.4236009976908201e-016 0.91752050034918575 0.39768848542418211 0
		 -4.0951723353960473e-016 -0.39768848542418211 0.91752050034918575 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 3.6675699561413695e-015 150.55119273242795 -0.48014248098381662 1;
createNode joint -n "NeckPart1_M" -p "Neck_M";
	rename -uid "EB37F011-4DE8-3BA4-F2E6-1C8B24AF58E3";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.28247023262624 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.2346839095951623 2.1316282072803006e-014 -3.7046243550941875e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.4236009976908201e-016 0.91752050034918575 0.39768848542418211 0
		 -4.0951723353960473e-016 -0.39768848542418211 0.91752050034918575 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 1.7404151266526132e-016 151.68404053093278 0.010877093000710825 1;
createNode joint -n "NeckPart2_M" -p "NeckPart1_M";
	rename -uid "38C882C9-4B80-439D-573E-4784F8253376";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.28247023262624 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.2346839095957591 -7.815970093361102e-014 -4.6641665082914267e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.4236009976908201e-016 0.91752050034918575 0.39768848542418211 0
		 -4.0951723353960473e-016 -0.39768848542418211 0.91752050034918575 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -4.2790290840079843e-015 152.81688832943823 0.50189666698540214 1;
createNode joint -n "Head_M" -p "NeckPart2_M";
	rename -uid "BF8FD79F-489D-DF54-F683-0B9BE5D9ECEE";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.28247023262624 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.2346839095955318 2.1316282072803006e-014 -7.6300299620929196e-015 ;
	setAttr ".r" -type "double3" 0 0 1.2722218725854064e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -23.433753848155312 ;
	setAttr ".bps" -type "matrix" 2.9347859833135462e-016 1.0000000000000002 -5.5511151231257827e-017 0
		 -3.1912548455687079e-016 5.5511151231257827e-017 1.0000000000000002 0 1 -2.7755575615628909e-016 3.3306690738754696e-016 0
		 -1.1697963134482775e-014 153.94973612794337 0.99291624097006514 1;
createNode joint -n "Eye_R" -p "Head_M";
	rename -uid "F85076AE-4FEA-449F-DF95-19A3B0F36B00";
	addAttr -ci true -sn "fat" -ln "fat" -dv 2.0515438953913994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 9.7514551503604707 10.789890620989423 -5.0983098705966956 ;
	setAttr ".r" -type "double3" 0 0 8.2694421718051442e-014 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 90.000000000000014 ;
	setAttr ".ssc" no;
createNode joint -n "EyeEnd_R" -p "Eye_R";
	rename -uid "F3599588-4043-5D38-9E4C-CC8AD0779A5C";
	addAttr -ci true -sn "fat" -ln "fat" -dv 2.0515438953913994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 1.7527381797653145 -8.5265128291212022e-014 8.8817841970012523e-015 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 15.94374013502415 -0.26038586000779179 -0.018143823894148849 ;
createNode joint -n "Jaw_M" -p "Head_M";
	rename -uid "035B39E8-4CBD-9283-F6C8-188EB58FA790";
	addAttr -ci true -sn "fat" -ln "fat" -dv 2.0515438953913994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -2.8811861827678626 4.159858809943862 -2.0688161726652351e-014 ;
	setAttr ".r" -type "double3" 0 0 2.5444437451708134e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 97.931554420298852 ;
	setAttr ".ssc" no;
createNode joint -n "JawEnd_M" -p "Jaw_M";
	rename -uid "7D2E008A-4F0B-BD18-1A40-8C869CEED4F1";
	addAttr -ci true -sn "fat" -ln "fat" -dv 2.0515438953913994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 9.7760181901505199 0 -4.9864579455724936e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "HeadEnd_M" -p "Head_M";
	rename -uid "A6DD4F14-4AEC-E9CE-76D7-82A624E822C5";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.5902018169349499 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 24.492310991197172 -2.7866597918091429e-014 -6.8440518462405743e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "Eye_L" -p "Head_M";
	rename -uid "1C7D3ACF-47FD-1647-B2C0-DFBBD38EC1C4";
	addAttr -ci true -sn "fat" -ln "fat" -dv 2.0515438953913994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 9.7514551503604707 10.789890620989448 5.0983098705966023 ;
	setAttr ".r" -type "double3" 0 0 1.0813885916975958e-013 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".ssc" no;
createNode joint -n "EyeEnd_L" -p "Eye_L";
	rename -uid "2F6C1951-499D-935E-12D7-56A357D27ACF";
	addAttr -ci true -sn "fat" -ln "fat" -dv 2.0515438953913994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" 1.7527381797653323 -2.8421709430404007e-013 -2.3980817331903381e-014 ;
	setAttr ".ro" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.943740135024125 0.2603858600078417 -0.018143823894150517 ;
createNode joint -n "Scapula_L" -p "Chest_M";
	rename -uid "2FFAD566-4A4E-31BD-BA3A-7CA0F0060776";
	addAttr -ci true -sn "fat" -ln "fat" -dv 6.6675176600220505 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.1944024239794828 -1.4630365309524791 8.4006089389264602 ;
	setAttr ".r" -type "double3" -3.1507369813247956e-014 1.0931314816264841e-029 -3.9756933518293955e-014 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -163.59619647900038 73.611757129208442 13.304616761790152 ;
	setAttr ".bps" -type "matrix" -0.95937189098325415 0.27895312508270781 0.042317003648725884 0
		 -0.079679084802482605 -0.12398856345646331 -0.98907941014715384 0 -0.27065996792332225 -0.95226676416779021 0.14117787229290699 0
		 8.4006089389264353 139.5099833961379 -1.0444591400009147 1;
createNode joint -n "Shoulder_L" -p "Scapula_L";
	rename -uid "8C1D36A8-4F9A-9164-22D6-50AC344DED06";
	addAttr -ci true -sn "fat" -ln "fat" -dv 6.6675176600220505 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -11.2850226203816 1.1119993814645568e-012 -2.8421709430404007e-013 ;
	setAttr ".r" -type "double3" -6.3611093629270335e-015 1.2821611059649799e-014 6.7586786981099735e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 41.559621793263688 -10.207505970295204 ;
	setAttr ".bps" -type "matrix" -0.51638190189616995 0.85360146636234135 0.068660527365840662 0
		 -0.2484316496489363 -0.072592016795136438 -0.96592552225848305 0 -0.81953123604094702 -0.51584390635314814 0.24954682412629869 0
		 19.227142430030732 136.3619910695536 -1.5220074834047119 1;
	setAttr -k on ".twistAmount";
	setAttr -k on ".twistAddition";
createNode joint -n "ShoulderPart1_L" -p "Shoulder_L";
	rename -uid "C78001DD-449D-9F4D-1586-6EA195B48EED";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.2660061136377578 -2.3092638912203256e-014 -7.1054273576010019e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.51638190189616995 0.85360146636234135 0.068660527365840662 0
		 -0.2484316496489363 -0.072592016795136438 -0.96592552225848305 0 -0.81953123604094702 -0.51584390635314814 0.24954682412629869 0
		 22.9791763409049 130.15971783485463 -2.0208952790973278 1;
	setAttr -k on ".twistAmount" 0.33333333333333331;
	setAttr -k on ".twistAddition";
createNode joint -n "ShoulderPart2_L" -p "ShoulderPart1_L";
	rename -uid "5F73C193-4666-E3EF-45FC-1F9DC04D78C8";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.2660061136378005 -1.9539925233402755e-014 -5.6843418860808015e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.51638190189616995 0.85360146636234135 0.068660527365840662 0
		 -0.2484316496489363 -0.072592016795136438 -0.96592552225848305 0 -0.81953123604094702 -0.51584390635314814 0.24954682412629869 0
		 26.73121025177905 123.9574446001557 -2.5197830747899417 1;
	setAttr -k on ".twistAmount" 0.66666666666666663;
	setAttr -k on ".twistAddition";
createNode joint -n "Elbow_L" -p "ShoulderPart2_L";
	rename -uid "5E5C1AB9-420A-C602-EFB2-A8B17FCBBCF1";
	addAttr -ci true -sn "fat" -ln "fat" -dv 4.615973764630648 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.2660061136377294 -1.7763568394002505e-014 -7.1054273576010019e-014 ;
	setAttr ".r" -type "double3" 0 0 3.1805546814635168e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 14.707844589729389 ;
	setAttr ".bps" -type "matrix" -0.56253596761340741 0.80720123390250953 -0.17882799872367228 0
		 -0.10918717092426589 -0.2869341950074803 -0.95170737595174959 0 -0.81953123604094702 -0.51584390635314814 0.24954682412629869 0
		 30.483244162653243 117.75517136545672 -3.0186708704825631 1;
	setAttr -k on ".twistAmount";
	setAttr -k on ".twistAddition";
createNode joint -n "ElbowPart1_L" -p "Elbow_L";
	rename -uid "4970791D-43C7-C5AB-71C7-FBB3C047E967";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.9778149385249719 7.1054273576010019e-015 1.4210854715202004e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.56253596761340741 0.80720123390250953 -0.17882799872367228 0
		 -0.10918717092426589 -0.2869341950074803 -0.95170737595174959 0 -0.81953123604094702 -0.51584390635314814 0.24954682412629869 0
		 34.408516071066458 112.12267049351711 -1.7708421807362829 1;
	setAttr -k on ".twistAmount" 0.33333333333333331;
	setAttr -k on ".twistAddition";
createNode joint -n "ElbowPart2_L" -p "ElbowPart1_L";
	rename -uid "DF816A85-4147-DFEF-C4D0-D58733092FCA";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.9778149385249435 1.4210854715202004e-014 2.8421709430404007e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.56253596761340741 0.80720123390250953 -0.17882799872367228 0
		 -0.10918715090580919 -0.28693418240710766 -0.95170738204735861 0 -0.8195312387080308 -0.51584391336200797 0.24954680087921294 0
		 38.333787979479659 106.49016962157748 -0.5230134909900126 1;
	setAttr -k on ".twistAmount" 0.66666666666666663;
	setAttr -k on ".twistAddition";
createNode joint -n "Wrist_L" -p "ElbowPart2_L";
	rename -uid "70707A40-41D0-71EC-2B93-2BB9139D5671";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.7438123110826886 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 2.3100000000000005 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.977814938524979 0 1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" -2.4997171949627336e-014 -2.201540193575527e-014 -4.2738703532166011e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -13.521250444602389 8.3330281096855021 -4.3398433712008 ;
	setAttr ".bps" -type "matrix" -0.42805401778951424 0.89263225613070396 -0.14134147717235615 0
		 0.061070304277066584 -0.1274669900345336 -0.98996090043346807 0 -0.90168740469730446 -0.43238850790295691 4.9433730391484909e-005 0
		 42.259059887892874 100.8576687496379 0.72481519875625344 1;
createNode joint -n "MiddleFinger1_L" -p "Wrist_L";
	rename -uid "1144E07E-485D-0A66-75F4-8F9D674CA2EA";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -11.622556951389683 1.4566126083082054e-013 -1.1368683772161603e-013 ;
	setAttr ".r" -type "double3" 7.7526020360673219e-015 6.8704950736301746e-015 -2.2611755938529692e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.24701796629516376 14.054891263265455 -7.7773719725675754 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.20046082362963413 0.97968391885271067 -0.0059057032709221823 0
		 -0.0016413236396655689 -0.0063638860409269893 -0.99997840327237475 0 -0.97970034410856377 -0.20044680116143904 0.0028836882126624603 0
		 47.234142087922791 90.482999516111363 2.3675645667853633 1;
createNode joint -n "MiddleFinger2_L" -p "MiddleFinger1_L";
	rename -uid "D0978E85-4799-759E-1F76-35859D608D08";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.0193352100693005 7.5495165674510645e-015 1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 9.5091479976897931e-015 1.1931157452482355e-014 1.6527469755275927e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.03823241732443862 7.0462296279878469 0.014371144228007279 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.078767258149763777 0.99687207743158701 -0.0064637667656412658 0
		 -0.0022562503368681987 -0.0066621642525707767 -0.99997526214496391 0 -0.99689047963052857 -0.078750725740807451 0.0027739533720378437 0
		 48.039861334576869 86.545321446328003 2.3913015678823926 1;
createNode joint -n "MiddleFinger3_L" -p "MiddleFinger2_L";
	rename -uid "597BF1D5-4991-DC18-E44B-84B8B55101EE";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.4939868148700413 1.0658141036401503e-013 8.5265128291212022e-014 ;
	setAttr ".r" -type "double3" 1.1769632018907712e-014 -1.9881053331798478e-014 -7.3246520363550201e-015 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.052362469576947429 -1.8461493596732201 -0.0073031615319470921 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.11084171874212204 0.99381845937857516 -0.0062436515507937676 0
		 -0.0031745530189044723 -0.0066363785539233829 -0.99997293998028736 0 -0.99383300186672308 -0.11081889856014815 0.0038905169956034262 0
		 48.315073095995501 83.062263551669872 2.4138858837358308 1;
createNode joint -n "MiddleFinger4_L" -p "MiddleFinger3_L";
	rename -uid "78ABE551-427C-8476-D3C4-07AEEF85F0A2";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -2.7372071378116232 -2.8421709430404007e-014 0 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "ThumbFinger1_L" -p "Wrist_L";
	rename -uid "88806988-40CB-EE01-95DF-5FBDDAE85FD6";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.6219143871220325 -4.2433636455690618 2.081945725422969 ;
	setAttr ".r" -type "double3" 2.9022561468354588e-014 -3.1805546814635049e-015 4.6913181551586881e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -65.013753730819161 23.922612860060351 18.134507052022766 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011165504885745248 0.91448913800532161 -0.40445636102171784 0
		 0.97040915752910095 -0.10748018125672243 -0.21622691234137012 0 -0.24120820567366025 -0.39007387391019388 -0.88862870447020093 0
		 42.529135182098699 95.48004601225955 5.720291896546474 1;
createNode joint -n "ThumbFinger2_L" -p "ThumbFinger1_L";
	rename -uid "F5AF08EE-4487-E8E5-79EE-1DA751ADA514";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.6060315911739593 -5.6843418860808015e-014 7.815970093361102e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011165504885745248 0.91448913800532161 -0.40445636102171784 0
		 0.97040915752910095 -0.10748018125672243 -0.21622691234137012 0 -0.24120820567366025 -0.39007387391019388 -0.88862870447020093 0
		 42.488872018749227 92.182369290826841 7.1787743116420124 1;
createNode joint -n "ThumbFinger3_L" -p "ThumbFinger2_L";
	rename -uid "466FBFAA-4A69-A751-F9B8-A4AAEBF2618B";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.6857353204952972 -3.907985046680551e-014 -3.5527136788005009e-013 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011165504885745248 0.91448913800532161 -0.40445636102171784 0
		 0.97040915752910095 -0.10748018125672243 -0.21622691234137012 0 -0.24120820567366025 -0.39007387391019388 -0.88862870447020093 0
		 42.447718923020709 88.811804374671468 8.6694934070590755 1;
createNode joint -n "ThumbFinger4_L" -p "ThumbFinger3_L";
	rename -uid "C5919747-481F-E65F-AEFB-679FA1AA4EA8";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -3.2303742869033272 3.7872524885074199e-006 2.4202093342751141e-006 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "IndexFinger1_L" -p "Wrist_L";
	rename -uid "6EE6FB0A-49A8-2ADE-3BD7-22BB15CEAF09";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -12.217774799299249 -2.2419819373604 0.87772441849487848 ;
	setAttr ".r" -type "double3" 1.530641940454313e-014 4.4515341498764781e-014 1.118660716870996e-013 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.64306410152709026 21.37555831033308 5.5803899526520455 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.062542916656711689 0.97334415359666226 -0.22065706930726009 0
		 0.11354162688820568 -0.21271545584500551 -0.97049494270100711 0 -0.99156274765626962 -0.085751346950638963 -0.097211233694980026 0
		 46.560575907130016 89.857949603246666 4.6712113833055282 1;
createNode joint -n "IndexFinger2_L" -p "IndexFinger1_L";
	rename -uid "040E7CDB-4A93-4409-5B89-CEAD23AC4DE2";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.7112077937487271 -3.5527136788005009e-015 1.3500311979441904e-013 ;
	setAttr ".r" -type "double3" 2.0197042367565148e-010 -8.6307887874646104e-014 -8.6405884760583404e-012 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.0012331907375704777 -2.4827117732439437 0.02846835619587083 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.10538029191818626 0.96861022871496416 -0.22514266344694153 0
		 0.11359395167864834 -0.2131963003628502 -0.9703833014090989 0 -0.9879227744197755 -0.12783412040741807 -0.087561575147977716 0
		 46.730142750213339 87.219011348015627 5.2694585493571191 1;
createNode joint -n "IndexFinger3_L" -p "IndexFinger2_L";
	rename -uid "254DEB19-4DC5-FF31-564E-9884402A331A";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.1608979938010719 8.8107299234252423e-013 -1.0658141036401503e-013 ;
	setAttr ".r" -type "double3" 2.015258126477355e-010 -2.4972624758105686e-013 1.6110279752200072e-011 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.6269906615827694 7.0421664309702905 -0.081032153644978899 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.016374442467800454 0.97727393722498035 -0.21134694049040301 0
		 0.14160446883956571 -0.21151135102976704 -0.96706314312470154 0 -0.98978788234577475 -0.014092551449184934 -0.14184973724021813 0
		 47.063239103523891 84.157333219295154 5.9811115425647294 1;
createNode joint -n "IndexFinger4_L" -p "IndexFinger3_L";
	rename -uid "313B491C-41A0-1847-5E90-059F40432A4B";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -3.0498988820507407 3.1974423109204508e-014 -4.2632564145606011e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "Cup_L" -p "Wrist_L";
	rename -uid "C00E504F-47F8-2D40-E62D-AA9055B62F82";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.23092633723484 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.9195468362661217 1.3180287923802378 -0.1026297234232203 ;
	setAttr ".r" -type "double3" -1.8611505691729276e-014 8.1697476351756544e-015 6.0260628954335471e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.0014439751562973138 0.68668985185053044 0.12048458776555422 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.41708745257772278 0.89748020134709539 -0.1434131970642977 0
		 0.061947451084991577 -0.12935440777533991 -0.98966153329972562 0 -0.90675276134473293 -0.42165948984822837 -0.0016445104539811455 0
		 43.253761971846657 99.02059007646703 -0.30867525937642282 1;
createNode joint -n "PinkyFinger1_L" -p "Cup_L";
	rename -uid "47D20535-4E23-026E-FBF5-4394799A6B3F";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -8.4115546922501068 3.1218164334996485 0.024367626743980964 ;
	setAttr ".r" -type "double3" 2.9420130803537534e-014 1.162890305410099e-014 1.5405811738338909e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.8666739182808139 20.591376094394061 -29.127944866024929 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.050385210779783862 0.94113378304010764 0.33425818307902694 0
		 -0.11666099180693196 0.32684610218591709 -0.93784958201008772 0 -0.991892909302864 -0.086248640026892587 0.093325390801280689 0
		 46.933409048628469 91.057290720623982 -2.1919290197540962 1;
createNode joint -n "PinkyFinger2_L" -p "PinkyFinger1_L";
	rename -uid "EFD59549-407F-EE9E-087B-5F81F012AA78";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.4499301332412102 -1.7763568394002505e-014 0 ;
	setAttr ".r" -type "double3" 3.0431137198866034e-014 3.1727192848368938e-014 -3.7160308797880391e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.25314265926258722 20.082497249706911 -0.025671567371473799 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.29331639688437655 0.9133898944327552 0.28228423984857332 0
		 -0.12087466564401021 0.32833421063497908 -0.93679558140084862 0 -0.94834319026616909 0.24065649144543186 0.20671150572950514 0
		 47.056849294787568 88.751578706142681 -3.0108382147618586 1;
createNode joint -n "PinkyFinger3_L" -p "PinkyFinger2_L";
	rename -uid "5E617CF1-4A0D-106D-6729-56B5C650ABED";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.2517172873994866 -2.1316282072803006e-014 -2.4868995751603507e-014 ;
	setAttr ".r" -type "double3" 2.0759797218976336e-015 4.4862438164442065e-015 2.7109259042786694e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.1500272209346534 -3.7268268235111881 -0.16120539085997773 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.23139245677998366 0.92617546234611536 0.29775248763575823 0
		 -0.15618354188395622 0.33745420030694689 -0.92829486906897285 0 -0.96024175715801141 0.16829639224641141 0.22273772057497623 0
		 46.396383693245319 86.694882890712478 -3.6464625175892791 1;
createNode joint -n "PinkyFinger4_L" -p "PinkyFinger3_L";
	rename -uid "6E9BE318-4B1C-1BF2-67D8-7B883620D693";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -2.2660312317578359 -1.0658141036401503e-014 -5.4711790653527714e-013 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "RingFinger1_L" -p "Cup_L";
	rename -uid "664CC3F3-4326-C1A6-8D0C-D48D14A76196";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.825776063916571 1.2976222365335701 0.013665685612593848 ;
	setAttr ".r" -type "double3" -3.7769086842379307e-015 -1.8039708583925883e-014 -2.8873472967660988e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.31313100137460392 6.0934151531039857 -15.716307750779071 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.31965968223652996 0.93864646959619613 0.12946232141838748 0
		 -0.058516190628256512 0.11681432636236351 -0.99142839811600358 0 -0.94572381961479535 -0.32449532858132846 0.01758518530176352 0
		 47.419962871804358 90.02853517428494 -0.1837585860267793 1;
createNode joint -n "RingFinger2_L" -p "RingFinger1_L";
	rename -uid "E32A0598-488B-647B-236F-E78DDA670B93";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.9819387449465182 1.5099033134902129e-014 -1.4210854715202004e-013 ;
	setAttr ".r" -type "double3" -7.8147222446896587e-015 9.4636255323087406e-015 3.9359364183111021e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.18148233733574676 24.27272342856552 0.19982687626789788 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.097182806528062826 0.98942912274240125 0.10763602177956647 0
		 -0.054253473508219345 0.1132536436221655 -0.9920837529254255 0 -0.99378672899552334 0.090573855364038391 0.064686273635696609 0
		 48.373168463462868 87.229548898788806 -0.56980729827501164 1;
createNode joint -n "RingFinger3_L" -p "RingFinger2_L";
	rename -uid "89E3C40E-4C5A-9744-FE54-ED8D2C078675";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.7288466880779936 -1.6875389974302379e-014 2.4868995751603507e-013 ;
	setAttr ".r" -type "double3" 3.0758220723113146e-014 2.2654172393479601e-014 -9.587089446945634e-014 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.48486173250852499 -1.1387291408775275 -0.0013569562276108357 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.077415111804550435 0.99103103379689306 0.10892378305838581 0
		 -0.062673666219814669 0.11387293931841083 -0.99151649772132044 0 -0.99502709110197385 0.069931707704351614 0.070927034554511867 0
		 48.10797148373041 84.529548514105372 -0.86352949982603611 1;
createNode joint -n "RingFinger4_L" -p "RingFinger3_L";
	rename -uid "ED50F715-4EA1-30DD-56D3-41A1B8DC4CD3";
	addAttr -ci true -sn "fat" -ln "fat" -dv 1.2309263372348391 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -2.7256461682159738 8.7041485130612273e-014 0 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
createNode joint -n "Hip_L" -p "Root_M";
	rename -uid "85ED89DA-4326-F3B1-7581-959DD21EC54F";
	addAttr -ci true -sn "fat" -ln "fat" -dv 8.9242159449525893 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.0547977341200152 -0.82778875555604969 8.4081152751406769 ;
	setAttr ".r" -type "double3" 2.5593526799588869e-015 3.9756878980584037e-016 -2.4418523318709472e-005 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -174.45311017590799 1.9961189625327196 8.126909286303631 ;
	setAttr ".bps" -type "matrix" -0.034831759833711333 0.99934959032840764 0.0093351388490382926 0
		 -0.096601694743973371 0.0059303647300032172 -0.99530545228425304 0 -0.99471345677007861 -0.035570030708635958 0.09633229902741787 0
		 8.4081152751406787 92.882590783986231 4.196672440704007 1;
	setAttr -k on ".twistAmount";
	setAttr -k on ".twistAddition";
createNode joint -n "HipPart1_L" -p "Hip_L";
	rename -uid "714E5870-44D8-C188-D479-0A997464D9EE";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -12.092250823974609 -3.1510261067069223e-009 0 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.034831759833711333 0.99934959032840764 0.0093351388490382926 0
		 -0.096601694743973371 0.0059303647300032172 -0.99530545228425304 0 -0.99471345677007861 -0.035570030708635958 0.09633229902741787 0
		 8.82930965199475 80.798204876880177 4.0837896034010397 1;
	setAttr -k on ".twistAmount" 0.33333333333333331;
	setAttr -k on ".twistAddition";
createNode joint -n "HipPart2_L" -p "HipPart1_L";
	rename -uid "D794A517-4262-7C09-FF8B-48AA356FE98F";
	addAttr -ci true -k true -sn "twistAmount" -ln "twistAmount" -min 0 -max 1 -at "double";
	addAttr -ci true -k true -sn "twistAddition" -ln "twistAddition" -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -12.092250823974595 -3.1510252185285026e-009 1.7763568394002505e-015 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.034831759833711333 0.99934959032840764 0.0093351388490382926 0
		 -0.096601694743973371 0.0059303647300032172 -0.99530545228425304 0 -0.99471345677007861 -0.035570030708635958 0.09633229902741787 0
		 9.2505040288488232 68.713818969774124 3.9709067660980719 1;
	setAttr -k on ".twistAmount" 0.66666666666666663;
	setAttr -k on ".twistAddition";
createNode joint -n "Knee_L" -p "HipPart2_L";
	rename -uid "401C6BFF-4B3A-B843-3651-8B92D9AB9794";
	addAttr -ci true -sn "fat" -ln "fat" -dv 6.1546316861741994 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -12.092250823974616 -3.1510278830637617e-009 0 ;
	setAttr ".r" -type "double3" 0 0 4.2915613917443681e-005 ;
	setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -6.3511207478296967 ;
	setAttr ".bps" -type "matrix" -0.02393187383771965 0.99256029794332568 0.11937889411982464 0
		 -0.099861926354024577 0.11644238000849828 -0.98816434250726737 0 -0.99471345677007861 -0.035570030708635958 0.09633229902741787 0
		 9.6716984057029016 56.629433062668049 3.8580239287951037 1;
createNode joint -n "Ankle_L" -p "Knee_L";
	rename -uid "2EC127D6-44CD-1474-2DE4-3895FC307E74";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.7953562064740889 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -47.881469726562514 -1.2477186173143195e-008 3.3395508580724709e-013 ;
	setAttr ".r" -type "double3" -2.9317919745230678e-014 2.0461890344583196e-006 -1.5457529294688466e-005 ;
	setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.2252878497277742 2.0384426397554383 6.6910983514863176 ;
	setAttr ".bps" -type "matrix" 1.3440482615756366e-009 0.99999999999999878 -5.0931027642271004e-008 0
		 0.012108284039572259 -5.0943568119608124e-008 -0.99992669204177898 0 -0.99992669204178031 7.2726235450515375e-010 -0.012108284039572315 0
		 10.817591699609254 9.1041872034539537 -1.8580129636642488 1;
createNode joint -n "Toes_L" -p "Ankle_L";
	rename -uid "227AE156-40FC-5797-AC72-ACA8F6732BAB";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.0773158430870993 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.8328421364069412 -13.770143362656217 -6.5298877416353207e-011 ;
	setAttr ".r" -type "double3" -4.4726550208083668e-016 4.4726550208080694e-015 7.570007447848051e-013 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.050299695542388438 -0.69199855230507989 85.842518566502378 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -9.3313077036485947e-007 0.07249274257810967 -0.99736893989768571 0
		 -6.9171298486682235e-008 -0.99736893989812203 -0.072492742578076724 0 -0.99999999999956246 1.3440958896916858e-009 9.3569006435340052e-007 0
		 10.650858883390205 2.2713457685472616 11.9111212859021 1;
createNode joint -n "ToesEnd_L" -p "Toes_L";
	rename -uid "2BF4087D-4096-BE18-9FA5-F7ACF38597AE";
	addAttr -ci true -sn "fat" -ln "fat" -dv 3.0773158430870993 -at "double";
	addAttr -ci true -sn "fatY" -ln "fatY" -dv 1 -at "double";
	addAttr -ci true -sn "fatZ" -ln "fatZ" -dv 1 -at "double";
	setAttr ".t" -type "double3" -11.371045390366755 -6.4392935428259079e-014 5.4254464032510441e-008 ;
	setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.9341138516841897e-006 -0.0001083952827977495 0 ;
	setAttr ".ssc" no;
select -ne :time1;
	setAttr ".o" 119;
	setAttr ".unw" 119;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
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
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "Root_M.s" "Hip_R.is";
connectAttr "Hip_R.s" "HipPart1_R.is";
connectAttr "HipPart1_R.s" "HipPart2_R.is";
connectAttr "HipPart2_R.s" "Knee_R.is";
connectAttr "Knee_R.s" "Ankle_R.is";
connectAttr "Ankle_R.s" "Toes_R.is";
connectAttr "Toes_R.s" "ToesEnd_R.is";
connectAttr "Root_M.s" "RootPart1_M.is";
connectAttr "RootPart1_M.s" "RootPart2_M.is";
connectAttr "RootPart2_M.s" "Spine1_M.is";
connectAttr "Spine1_M.s" "Spine1Part1_M.is";
connectAttr "Spine1Part1_M.s" "Spine1Part2_M.is";
connectAttr "Spine1Part2_M.s" "Chest_M.is";
connectAttr "Chest_M.s" "Scapula_R.is";
connectAttr "Scapula_R.s" "Shoulder_R.is";
connectAttr "Shoulder_R.s" "ShoulderPart1_R.is";
connectAttr "ShoulderPart1_R.s" "ShoulderPart2_R.is";
connectAttr "ShoulderPart2_R.s" "Elbow_R.is";
connectAttr "Elbow_R.s" "ElbowPart1_R.is";
connectAttr "ElbowPart1_R.s" "ElbowPart2_R.is";
connectAttr "ElbowPart2_R.s" "Wrist_R.is";
connectAttr "Wrist_R.s" "MiddleFinger1_R.is";
connectAttr "MiddleFinger1_R.s" "MiddleFinger2_R.is";
connectAttr "MiddleFinger2_R.s" "MiddleFinger3_R.is";
connectAttr "MiddleFinger3_R.s" "MiddleFinger4_R.is";
connectAttr "Wrist_R.s" "ThumbFinger1_R.is";
connectAttr "ThumbFinger1_R.s" "ThumbFinger2_R.is";
connectAttr "ThumbFinger2_R.s" "ThumbFinger3_R.is";
connectAttr "ThumbFinger3_R.s" "ThumbFinger4_R.is";
connectAttr "Wrist_R.s" "IndexFinger1_R.is";
connectAttr "IndexFinger1_R.s" "IndexFinger2_R.is";
connectAttr "IndexFinger2_R.s" "IndexFinger3_R.is";
connectAttr "IndexFinger3_R.s" "IndexFinger4_R.is";
connectAttr "Wrist_R.s" "Cup_R.is";
connectAttr "Cup_R.s" "PinkyFinger1_R.is";
connectAttr "PinkyFinger1_R.s" "PinkyFinger2_R.is";
connectAttr "PinkyFinger2_R.s" "PinkyFinger3_R.is";
connectAttr "PinkyFinger3_R.s" "PinkyFinger4_R.is";
connectAttr "Cup_R.s" "RingFinger1_R.is";
connectAttr "RingFinger1_R.s" "RingFinger2_R.is";
connectAttr "RingFinger2_R.s" "RingFinger3_R.is";
connectAttr "RingFinger3_R.s" "RingFinger4_R.is";
connectAttr "Chest_M.s" "Neck_M.is";
connectAttr "Neck_M.s" "NeckPart1_M.is";
connectAttr "NeckPart1_M.s" "NeckPart2_M.is";
connectAttr "NeckPart2_M.s" "Head_M.is";
connectAttr "Head_M.s" "Eye_R.is";
connectAttr "Eye_R.s" "EyeEnd_R.is";
connectAttr "Head_M.s" "Jaw_M.is";
connectAttr "Jaw_M.s" "JawEnd_M.is";
connectAttr "Head_M.s" "HeadEnd_M.is";
connectAttr "Head_M.s" "Eye_L.is";
connectAttr "Eye_L.s" "EyeEnd_L.is";
connectAttr "Chest_M.s" "Scapula_L.is";
connectAttr "Scapula_L.s" "Shoulder_L.is";
connectAttr "Shoulder_L.s" "ShoulderPart1_L.is";
connectAttr "ShoulderPart1_L.s" "ShoulderPart2_L.is";
connectAttr "ShoulderPart2_L.s" "Elbow_L.is";
connectAttr "Elbow_L.s" "ElbowPart1_L.is";
connectAttr "ElbowPart1_L.s" "ElbowPart2_L.is";
connectAttr "ElbowPart2_L.s" "Wrist_L.is";
connectAttr "Wrist_L.s" "MiddleFinger1_L.is";
connectAttr "MiddleFinger1_L.s" "MiddleFinger2_L.is";
connectAttr "MiddleFinger2_L.s" "MiddleFinger3_L.is";
connectAttr "MiddleFinger3_L.s" "MiddleFinger4_L.is";
connectAttr "Wrist_L.s" "ThumbFinger1_L.is";
connectAttr "ThumbFinger1_L.s" "ThumbFinger2_L.is";
connectAttr "ThumbFinger2_L.s" "ThumbFinger3_L.is";
connectAttr "ThumbFinger3_L.s" "ThumbFinger4_L.is";
connectAttr "Wrist_L.s" "IndexFinger1_L.is";
connectAttr "IndexFinger1_L.s" "IndexFinger2_L.is";
connectAttr "IndexFinger2_L.s" "IndexFinger3_L.is";
connectAttr "IndexFinger3_L.s" "IndexFinger4_L.is";
connectAttr "Wrist_L.s" "Cup_L.is";
connectAttr "Cup_L.s" "PinkyFinger1_L.is";
connectAttr "PinkyFinger1_L.s" "PinkyFinger2_L.is";
connectAttr "PinkyFinger2_L.s" "PinkyFinger3_L.is";
connectAttr "PinkyFinger3_L.s" "PinkyFinger4_L.is";
connectAttr "Cup_L.s" "RingFinger1_L.is";
connectAttr "RingFinger1_L.s" "RingFinger2_L.is";
connectAttr "RingFinger2_L.s" "RingFinger3_L.is";
connectAttr "RingFinger3_L.s" "RingFinger4_L.is";
connectAttr "Root_M.s" "Hip_L.is";
connectAttr "Hip_L.s" "HipPart1_L.is";
connectAttr "HipPart1_L.s" "HipPart2_L.is";
connectAttr "HipPart2_L.s" "Knee_L.is";
connectAttr "Knee_L.s" "Ankle_L.is";
connectAttr "Ankle_L.s" "Toes_L.is";
connectAttr "Toes_L.s" "ToesEnd_L.is";
// End of test_skeleton_externalA.ma
