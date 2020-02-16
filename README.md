# SoapAPIViewpoint-Python

SOAP API for Viewpoint, using python. See _Instructions for usage_ section below for changes required for usage as well as Sample code.

# Instructions for usage

1. In **viewpoint.py** file, replace the 'API_TOKEN'- _this is the main file, to query existing API's_
2. In **vpbusinessunits.py** file, replace 'webhook_url' with relevant webhook. -_this is a custom file that has been made, specifically for Business Units from the API.

## Business Unit Examples

#### **Business Units** using API_TOKEN that has been provided. Returns all information relating to Business Unit 

> _viewpoint.get_business_units()_ 

 #### ** Project / Projects ** information. 

_Note: Will need Business Unit ID to run the below command. Business Unit ID can be obtained from the above command._
> _viewpoint.get_projects('0000')_ 

#### Business Unit, filtering to only return 'ID'
> _viewpoint.get_business_units()[0]['ID']_

#### Business Unit, filtering to only return 'Name'
_viewpoint.get_business_units()[0]['Name']_

## Form Examples

### _Forms_ filtering for a specific time.
** Note ** : _This will only return a maximum of a 3 month period._
>  _viewpoint.get_forms('12680','2010-01-01','2020-02-15' )_ 

Example of status code, returned stating date range is out of range.
> "Status":{"Code":14,"Message":"You have supplied invalid information as follows: At least one of 
the created, status changed, last modified, or last modified on server date range must be supplied and be within 3 months.
