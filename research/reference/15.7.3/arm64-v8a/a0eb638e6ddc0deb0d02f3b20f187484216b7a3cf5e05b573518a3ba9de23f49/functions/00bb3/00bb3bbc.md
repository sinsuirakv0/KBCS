# 00bb3bbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bb3bbc",
  "name": "_ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE",
  "size": 632,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "685e8e5874ce54aaece91e77b8086e452b27e99d9b8e5c0785b3e1273fe75362",
  "source_text_sha256": "685e8e5874ce54aaece91e77b8086e452b27e99d9b8e5c0785b3e1273fe75362"
}
~~~

## 呼び出し元

- [00be1cc0](../00be1/00be1cc0.md)

## 呼び出し先

- [00b750e4](../00b75/00b750e4.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00be1620](../00be1/00be1620.md)
- [00be1ca0](../00be1/00be1ca0.md)

## 疑似コード / UTF-8 3449 bytes

~~~c

void _ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE
               (undefined8 *param_1,undefined8 param_2)

{
  undefined8 *puVar1;
  long lVar2;
  undefined8 local_100;
  undefined8 uStack_f8;
  undefined8 local_f0;
  char acStack_e4 [100];
  tm local_80;
  
  lVar2 = 0;
                    /* try { // try from 00bb3be8 to 00cb3bef has its CatchHandler @ 00bbac98 */
  puVar1 = param_1 + 0x16;
  local_80.tm_zone = (char *)0x0;
  local_80.tm_wday = 0;
  local_80.tm_yday = 0;
  local_80.tm_mon = 0;
  local_80.tm_year = 0;
  local_80.tm_gmtoff = 0;
  local_80.tm_isdst = 0;
  local_80._36_4_ = 0;
  local_80.tm_hour = 0;
  local_80.tm_mday = 0;
  local_80.tm_sec = 0;
  local_80.tm_min = 0;
  do {
    local_80.tm_wday = (int)lVar2;
    strftime_l(acStack_e4,100,"%A",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1 + -0x15,acStack_e4);
    strftime_l(acStack_e4,100,"%a",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1,acStack_e4);
    lVar2 = lVar2 + 1;
    puVar1 = puVar1 + 3;
  } while (lVar2 != 7);
  lVar2 = 0;
  puVar1 = param_1 + 0x4f;
  do {
    local_80.tm_mon = (int)lVar2;
    strftime_l(acStack_e4,100,"%B",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1 + -0x24,acStack_e4);
    strftime_l(acStack_e4,100,"%b",&local_80,(__locale_t)*param_1);
    FUN_00b750e4(puVar1,acStack_e4);
    lVar2 = lVar2 + 1;
    puVar1 = puVar1 + 3;
                    /* try { // try from 00bb3cd0 to 00cb3cdb has its CatchHandler @ 00bbaa00 */
  } while (lVar2 != 0xc);
                    /* try { // try from 00bb3cdc to 00cb3ceb has its CatchHandler @ 00bba9ec */
                    /* try { // try from 00bb3cec to 00cb3cff has its CatchHandler @ 00bba9c0 */
  local_80.tm_hour = 1;
  strftime_l(acStack_e4,100,"%p",&local_80,(__locale_t)*param_1);
  FUN_00b750e4(param_1 + 0x73,acStack_e4);
  local_80.tm_hour = 0xd;
  strftime_l(acStack_e4,100,"%p",&local_80,(__locale_t)*param_1);
  FUN_00b750e4(param_1 + 0x76,acStack_e4);
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,99,param_2);
  if ((*(byte *)(param_1 + 0x79) & 1) != 0) {
    _ZdlPv((void *)param_1[0x7b]);
  }
  param_1[0x7b] = local_f0;
  param_1[0x7a] = uStack_f8;
  param_1[0x79] = local_100;
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,0x72,param_2);
  if ((*(byte *)(param_1 + 0x7c) & 1) != 0) {
    _ZdlPv((void *)param_1[0x7e]);
  }
                    /* try { // try from 00bb3dac to 00cb3dc3 has its CatchHandler @ 00bbaba0 */
  param_1[0x7e] = local_f0;
  param_1[0x7d] = uStack_f8;
  param_1[0x7c] = local_100;
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,0x78,param_2);
  if ((*(byte *)(param_1 + 0x7f) & 1) != 0) {
    _ZdlPv((void *)param_1[0x81]);
  }
                    /* try { // try from 00bb3dd4 to 00cb3ddb has its CatchHandler @ 00bbad04 */
                    /* try { // try from 00bb3de4 to 00cb3df3 has its CatchHandler @ 00bbacf4 */
  param_1[0x81] = local_f0;
  param_1[0x80] = uStack_f8;
  param_1[0x7f] = local_100;
  _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE(&local_100,param_1,0x58,param_2);
                    /* try { // try from 00bb3dfc to 00cb3e07 has its CatchHandler @ 00bbacf0 */
  if ((*(byte *)(param_1 + 0x82) & 1) != 0) {
    _ZdlPv((void *)param_1[0x84]);
  }
  param_1[0x83] = uStack_f8;
  param_1[0x82] = local_100;
  param_1[0x84] = local_f0;
  return;
}

~~~
