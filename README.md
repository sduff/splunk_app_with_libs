# Splunk App with External Libraries
How to build a Splunk App with external Python Libraries

Refer to https://stackoverflow.com/questions/59899533/

    SPLUNK_HOME = /opt/splunk
    cd $SPLUNK_HOME
    git clone git@github.com:sduff/splunk_app_with_libs.git
    pip install pyOpenSSL -t $SPLUNK_HOME/etc/apps/splunk_app_with_libs/bin
    pip install boxsdk -t $SPLUNK_HOME/etc/apps/splunk_app_with_libs/bin
    pip install pyJWT -t $SPLUNK_HOME/etc/apps/splunk_app_with_libs/bin
    pip install boto3 -t $SPLUNK_HOME/etc/apps/splunk_app_with_libs/bin
    /opt/splunk/bin/splunk restart
    # Then log into splunk, and run the following search
    | searchcommand

Based off some code from the Splunk Add-On for AWS, https://splunkbase.splunk.com/app/1876/
