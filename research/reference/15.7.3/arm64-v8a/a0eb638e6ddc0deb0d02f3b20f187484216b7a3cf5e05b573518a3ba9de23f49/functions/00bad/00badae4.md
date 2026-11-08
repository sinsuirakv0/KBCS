# 00badae4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00badae4",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef01bcc00a1e68fae0c24df86f81f27bc0bef0f8373635c5a7fa9a621a96f12b",
  "source_text_sha256": "ef01bcc00a1e68fae0c24df86f81f27bc0bef0f8373635c5a7fa9a621a96f12b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1388 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  int iVar1;
  uint uVar2;
  undefined8 uVar3;
  byte *pbVar4;
  ulong uVar5;
  
  uVar5 = *(ulong *)(param_1 + 0x18);
  if ((*(byte *)(param_1 + 0x20) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00badb00:
      uVar3 = 1;
      goto LAB_00badbac;
    }
    param_6[0] = 0xff;
    param_6[1] = 0xfe;
    param_6 = param_6 + 2;
  }
  for (; param_3 < param_4; param_3 = param_3 + 1) {
    uVar2 = *param_3;
    if (uVar2 >> 0xb == 0x1b || uVar5 < uVar2) {
      uVar3 = 2;
      goto LAB_00badbac;
    }
    if ((uVar2 & 0xffff0000) == 0) {
      if (param_7 - (long)param_6 < 2) goto LAB_00badb00;
      pbVar4 = param_6 + 2;
      *(short *)param_6 = (short)uVar2;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00badb00;
      param_6[2] = (byte)uVar2;
      iVar1 = (uVar2 >> 10 & 0x7c0) + 0x3fc0;
      param_6[3] = (byte)(uVar2 >> 8) & 3 | 0xdc;
      pbVar4 = param_6 + 4;
      *param_6 = (byte)iVar1 | (byte)(uVar2 >> 10) & 0x3f;
      param_6[1] = (byte)((uint)iVar1 >> 8) | 0xd8;
    }
    param_6 = pbVar4;
  }
  uVar3 = 0;
LAB_00badbac:
  *param_5 = param_3;
  *param_8 = param_6;
  return uVar3;
}

~~~
