
class TagPathParse:
    def __init__(self, tag_path, write_path_a, write_path_b=''):
        """

        :type write_path_b: str
        """
        self.MachineName = tag_path.split("/")[1].upper().strip()
        self.SourcePath = tag_path
        self.WritePath_a = '[default]' + self.MachineName + '/' + self.MachineName + write_path_a
        if write_path_b != '':
            self.WritePath_b = '[default]' + self.MachineName + '/' + self.MachineName + write_path_b
        else:
            self.WritePath_b = ''


def get_machine_from_path(tag_path):

    # tag_path = tag_path.upper()
    # ret_val = tag_path.replace('[default]', '')
    try:
        ret_val = tag_path.split("/")
        ret_val = ret_val[0].strip()
        ret_val = ret_val + '\r\n' + 'gggg5'
        print(ret_val)
        return ret_val
    except:
        pass


tpp = TagPathParse('[default]D11/D11/Scanner/Scanner Message', '/MES/MES Control Hold', '/MES/MES Message')

g = get_machine_from_path('[default]D11/D11/Scanner/Scanner Message')
g = get_machine_from_path('[default]G08/G08/Gage/Count/Batch Bad Count')
print (g)

