# config.py
import configparser
ConfigPraser = configparser.ConfigParser()
ConfigPraser.read('config.ini')

Config = {
    'SCREEN_SIZE':          (int(ConfigPraser['general']['SCREEN_HEIGHT']), int(ConfigPraser['general']['SCREEN_WIDTH'])),
    'BACKGROUND_COLOR':     [int(x) for x in ConfigPraser['general']['BACKGROUND_COLOR'].split(', ')],

    'BLOCK_COLOR':          [int(x) for x in ConfigPraser['block']['BLOCK_COLOR'].split(', ')],
    'BLOCK_SIZE':           (int(ConfigPraser['block']['BLOCK_HEIGHT']), int(ConfigPraser['block']['BLOCK_WIDTH'])),
    'BLOCK_SPEED':          int(ConfigPraser['block']['BLOCK_SPEED']),
    'BLOCK_AMOUNT':         int(ConfigPraser['block']['BLOCK_AMOUNT']),

    'GRID_SIZE':            (int(ConfigPraser['grid']['GRID_ROWS']), int(ConfigPraser['grid']['GRID_COLS'])),
    'GRID_UPDATE_INTERVAL': int(ConfigPraser['grid']['GRID_UPDATE_INTERVAL']),
    'CAVE_SCALE':           int(ConfigPraser['cave']["CAVE_SCALE"]),
    'CAVE_THRESHOLD':       float(ConfigPraser['cave']["CAVE_THRESHOLD"]),
    'CELL_BORDER':          int(ConfigPraser['cave']["CELL_BORDER"]),
}
