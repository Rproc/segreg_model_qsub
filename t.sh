name="hey"
/lab/users/renan.procopio/usr/bin/xmlstarlet ed -P -u '//Repast:Param[@name="D"]/@value' -v 4  \
				-u '//Repast:Param[@name="FindspaceSteps"]/@value' -v 4 \
				-u '//Repast:Param[@name="Pred"]/@value' -v 5 \
				-u '//Repast:Param[@name="Log"]/@value' -v 1 \
				<old.xml >$name.xml
