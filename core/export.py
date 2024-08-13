from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import Submission

class submissionExport(resources.ModelResource):
    eventname = Field(
        attribute='event',
        widget=ForeignKeyWidget(Submission, 'name')
    )
    class Meta:
        model = Submission
        fields = ('id','eventname','teamname', 'participant1', 'mail1', 'participant2', 'mail2', 'participant3', 'mail3','contact')
        
# class consultancyexport(resources.ModelResource):

#     class Meta:
#         model=consultancy
#         fields = ('name','agency','startdate','date','amount','staffs','dept','date')
