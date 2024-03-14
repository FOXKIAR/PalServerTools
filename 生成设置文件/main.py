settings = {
    'Difficulty': 'None',  # 难度：1、2、3整数，简单、普通、困难，影响怪物血量、防御、攻击数值
    'DayTimeSpeedRate': '1.000000',  # 白天时间流逝速度，越大越快
    'NightTimeSpeedRate': '1.000000',  # 夜晚时间流逝速度，越大越快
    'ExpRate': '1.000000',  # 经验倍率，越大升级越快
    'PalCaptureRate': '1.000000',  # 帕鲁捕获基础概率倍数，越大越简单
    'PalSpawnNumRate': '1.000000',  # 帕鲁基础群居数量，越大数量越多。boos依旧生效
    'PalDamageRateAttack': '1.000000',  # 帕鲁基础伤害倍数，越大造成伤害越高。敌我都生效
    'PalDamageRateDefense': '1.000000',  # 帕鲁基础承伤倍数，越大越容易死。敌我都生效
    'PlayerDamageRateAttack': '1.000000',  # 玩家基础伤害倍数，越大造成伤害越高
    'PlayerDamageRateDefense': '1.000000',  # 玩家基础承伤倍数，越大越容易死
    'PlayerStomachDecreaceRate': '1.000000',  # 玩家饱食度降低速度，越大越容易饿
    'PlayerStaminaDecreaceRate': '1.000000',  # 玩家持久力降低速度，越大越容易虚
    'PlayerAutoHPRegeneRate': '1.000000',  # 玩家HP自动回复倍率，越大回复越快
    'PlayerAutoHpRegeneRateInSleep': '1.000000',  # 玩家睡眠时HP自动回复倍率，越大回复越快
    'PalStomachDecreaceRate': '1.000000',  # 帕鲁饱食度降低速度，越大越容易饿
    'PalStaminaDecreaceRate': '1.000000',  # 帕鲁持久力降低速度，越大越容易虚
    'PalAutoHPRegeneRate': '1.000000',  # 帕鲁HP自动回复倍率，越大回复越快
    'PalAutoHpRegeneRateInSleep': '1.000000',  # 帕鲁睡眠时HP自动回复倍率，越大回复越快
    'BuildObjectDamageRate': '1.000000',  # 对建筑伤害倍率，越大越容易摧毁建筑物
    'BuildObjectDeteriorationDamageRate': '1.000000',  # 建筑物风化速度，越大越容易风化
    'CollectionDropRate': '1.000000',  # 采集物掉落倍率，越大捡到的越多
    'CollectionObjectHpRate': '1.000000',  # 采集物生命倍率，越大越难挖矿
    'CollectionObjectRespawnSpeedRate': '1.000000',  # 采集物默认刷新时间，越大时间越长
    'EnemyDropItemRate': '1.000000',  # 敌方道具掉落倍率，越大捡到的越多
    'DeathPenalty': 'All',  # 死亡惩罚：None、Item、ItemAndEquipment、All，不掉落、物品、物品和装备、所有
    'bEnablePlayerToPlayerDamage': 'False',  # 玩家之间是否可以造成伤害：False、True，否、是
    'bEnableFriendlyFire': 'False',  # 该参数意义待定
    'bEnableInvaderEnemy': 'True',  # 是否会发生袭击：False、True，否、是
    'bActiveUNKO': 'False',  # 帕鲁是否产生粪便：False、True，否、是
    'bEnableAimAssistPad': 'True',  # 是否开启手柄辅助瞄准：同上
    'bEnableAimAssistKeyboard': 'False',  # 是否开启键盘辅助瞄准：同上
    'DropItemMaxNum': '3000',  # 世界内掉落物品数量上限，超过的自动删除
    'DropItemMaxNum_UNKO': '100',  # 粪便掉落上限
    'BaseCampMaxNum': '128',  # 营地最大数量
    'BaseCampWorkerMaxNum': '15',  # 可分派至据点工作的帕鲁数量上限，默认15。（01-28更新：实测该参数目前不生效）
    'DropItemAliveMaxHours': '1.000000',  # 掉落物品最大存在时间
    'bAutoResetGuildNoOnlinePlayers': 'False',  # 是否自动重置无在线玩家的工会
    'AutoResetGuildTimeNoOnlinePlayers': '72.000000',  # 自动重置时间，与上一个共用
    'GuildPlayerMaxNum': '20',  # 工会成员最大数量
    'PalEggDefaultHatchingTime': '72.000000',  # 默认孵蛋时间
    'WorkSpeedRate': '1.000000',  # 工作速度
    'bIsMultiplay': 'False',  # 是否多人游戏
    'bIsPvP': 'False',  # 是否可以pvp
    'bCanPickupOtherGuildDeathPenaltyDrop': 'False',  # 是否可以拾取其他工会的死亡掉落物
    'bEnableNonLoginPenalty': 'True',  # 是否启用不登录惩罚
    'bEnableFastTravel': 'True',  # 是否启用快速旅行
    'bIsStartLocationSelectByMap': 'True',  # 是否可以通过地图选择起始位置默认True即可，如果改为False则全部出生在初始台地
    'bExistPlayerAfterLogout': 'False',  # 注销后玩家是否仍然存在，就是是否删注销玩家的档，跟朋友一起玩的默认False即可
    'bEnableDefenseOtherGuildPlayer': 'False',  # 是否启用防御其他公会玩家功能，默认False即可。
    'CoopPlayerMaxNum': '4',  # 邀请码服务器玩家最大人数
    'ServerPlayerMaxNum': '32',  # 服务器玩家最大人数
    'ServerName': '"Default Palworld Server"',  # 服务器名称
    'ServerDescription': '""',  # 服务器简介
    'AdminPassword': '""',  # 管理员密码
    'ServerPassword': '""',  # 服务器密码
    'PublicPort': '8211',  # 服务器对外端口
    'PublicIP': '""',  # 服务器ip
    'RCONEnabled': 'False',  # 是否启用RCON
    'RCONPort': '25575',  # RCON端口号
    'Region': '""',  # 地区
    'bUseAuth': 'True',  # 使用授权
    'BanListURL': '"https://api.palworldgame.com/api/banlist.txt"',  # 封禁玩家
    'bShowPlayerList': 'False'  # 是否可以查看玩家列表
}

with open('./PalWorldSettings.ini', 'w') as outfile:
    outfile.write("[/Script/Pal.PalGameWorldSettings]\nOptionSettings=" + str(settings).replace("'", "").replace(": ", "=").replace("{", "(").replace("}", ")").replace(", ", ","))

print("以生成配置文件 ./PalWorldSettings.ini 。")
print("请将文件替换至 ~PalServer/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini")
print("或者 ~PalServer/Pal/Saved/Config/WindowsServer/PalWorldSettings.ini")