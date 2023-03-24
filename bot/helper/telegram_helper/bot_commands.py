from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = [f'start{CMD_SUFFIX}', 'start']
        self.MirrorCommand = [f'm{CMD_SUFFIX}', f'mirror{CMD_SUFFIX}']
        self.UnzipMirrorCommand = [f'uzm{CMD_SUFFIX}', f'unzipm{CMD_SUFFIX}']
        self.ZipMirrorCommand = [f'zm{CMD_SUFFIX}', f'zipmirror{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbm{CMD_SUFFIX}', f'qbmirror{CMD_SUFFIX}']
        self.QbUnzipMirrorCommand = [f'qbuzm{CMD_SUFFIX}', f'qbunzipm{CMD_SUFFIX}']
        self.QbZipMirrorCommand = [f'qbzm{CMD_SUFFIX}', f'qbzipmirror{CMD_SUFFIX}']
        self.YtdlCommand = [f'yt{CMD_SUFFIX}', f'ytdl{CMD_SUFFIX}']
        self.YtdlZipCommand = [f'ytz{CMD_SUFFIX}', f'ytdlzip{CMD_SUFFIX}']
        self.LeechCommand = [f'l{CMD_SUFFIX}', f'leech{CMD_SUFFIX}']
        self.UnzipLeechCommand = [f'uzl{CMD_SUFFIX}', f'unzipleech{CMD_SUFFIX}']
        self.ZipLeechCommand = [f'zl{CMD_SUFFIX}', f'zipleech{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbl{CMD_SUFFIX}', f'qbleech{CMD_SUFFIX}']
        self.QbUnzipLeechCommand = [f'qbuzl{CMD_SUFFIX}', f'qbunzipleech{CMD_SUFFIX}']
        self.QbZipLeechCommand = [f'qbzl{CMD_SUFFIX}', f'qbzipleech{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytl{CMD_SUFFIX}', f'ytdlleech{CMD_SUFFIX}']
        self.YtdlZipLeechCommand = [f'ytzl{CMD_SUFFIX}', f'ytdlzipleech{CMD_SUFFIX}']
        self.CloneCommand = f'c{CMD_SUFFIX}'
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del{CMD_SUFFIX}'
        self.CancelMirror = [f'can{CMD_SUFFIX}', f'cancel{CMD_SUFFIX}']
        self.CancelAllCommand = [f'canall{CMD_SUFFIX}', 'canallbot']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f'status{CMD_SUFFIX}', 's']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', 'auth']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', 'unauth']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'p{CMD_SUFFIX}', 'ping']
        self.RestartCommand = [f'rt{CMD_SUFFIX}', 'rtall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', 'stats']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bs{CMD_SUFFIX}', f'bsall']
        self.UserSetCommand = [f'us{CMD_SUFFIX}', f'usall']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.CategorySelect = f'catsel{CMD_SUFFIX}'
        self.RmdbCommand = f'rmdb{CMD_SUFFIX}'

BotCommands = _BotCommands()
