
import strFuncs	
import system
class GageAttention:
	def __init__(self, GageID):
		self.TagPathMaintenanceState = '[default]' + GageID + '/' + GageID + '/MES/Maint_State'
		self.TagPathStarved = '[default]' + GageID + '/' + GageID + '/Station Data/ST1/ST 1 Wait Time'
		self.Gage = GageID
			
	class GageStates:
		Running = 'Running/Standing By'.upper()
		Request = 'Request Maintenance'.upper()
		UnderMaintenance = 'Under Maintenance'.upper()
		ReadyToRun = 'Ready to Run'.upper()
		OutOfService = 'Scheduled Downtime'.upper()
		Starved = 'Starved'.upper()
			
	class StyleClasses:
		ColorHungry = 'WarningColors/ColorHungry'
		
		class BackgroundColors:
			MaintRequested = 'WarningColors/MaintRequestedBackground'
			UnderMaintenance = 'WarningColors/MaintInProcessBackground'
			MaintComplete = 'WarningColors/MaintReadyBackground'
			OutOfService = 'WarningColors/OutOfServiceBackground'
			
		class BorderColors:
			MaintRequested = 'WarningColors/MaintRequestedBorder'
			UnderMaintenance = 'WarningColors/MaintInProcessBorder'
			MaintComplete = 'WarningColors/MaintReadyBorder'
			OutOfService = 'WarningColors/OutOfServiceBorder'

	def GageIsInMaintenance(self):
		gageState = system.tag.readBlocking([self.TagPathMaintenanceState])[0].value
		if gageState == self.GageStates.Starved or gageState == '' or gageState == self.GageStates.Running:
			return False
		else:
			return True			

	def GetGageMaintState(self):
		maint_State = system.tag.readBlocking([self.TagPathMaintenanceState])[0].value
		if maint_State == '' or maint_State == self.GageStates.Starved:
			maint_State = self.GageStates.Running	
	
#		maint_State = system.db.runNamedQuery('Gage_States/maint_color_get', {'Gage':self.Gage})
#		maint_State = str(maint_State)
#		if maint_State == '':
#			maint_State = self.GageStates.Running
			
		return maint_State

	def GageIsStarved(self):
		retVal = system.tag.readBlocking([self.TagPathStarved])[0].value
		if strFuncs.isInteger(retVal) == False:
			return False

		retVal = int(retVal)
		return retVal > 30000
	
	def SetCardBackColor(self, classColor):
		system.tag.writeBlocking([self.TagPathMaintenanceState], [classColor])

	def GetGageBackgoundColor(self, maintState):

		if maintState.upper() == self.GageStates.Running:
			return ''

		if maintState.upper() == self.GageStates.Request:
			return self.StyleClasses.BackgroundColors.MaintRequested

		if maintState.upper() == self.GageStates.UnderMaintenance:
			return self.StyleClasses.BackgroundColors.UnderMaintenance

		if maintState.upper() == self.GageStates.ReadyToRun:
			return self.StyleClasses.BackgroundColors.MaintComplete

		if maintState.upper() == self.GageStates.OutOfService:
			return self.StyleClasses.BackgroundColors.OutOfService
		
		if maintState.upper() == self.GageStates.Starved:
			return self.StyleClasses.ColorHungry