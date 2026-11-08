# 00bad7fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bad7fc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb0EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "482c9c8351539c0a3f32d0d15480fc08863aebeb44c9132f2f96aebbf6138cdb",
  "source_text_sha256": "482c9c8351539c0a3f32d0d15480fc08863aebeb44c9132f2f96aebbf6138cdb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1450 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IwLb0EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  int iVar1;
  uint uVar2;
  byte bVar3;
  undefined8 uVar4;
  ulong uVar5;
  byte *pbVar6;
  long lVar7;
  
  uVar5 = *(ulong *)(param_1 + 0x18);
  if ((*(byte *)(param_1 + 0x20) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00bad818:
      uVar4 = 1;
      goto LAB_00bad8d4;
    }
    param_6[0] = 0xfe;
    param_6[1] = 0xff;
    param_6 = param_6 + 2;
  }
  for (; param_3 < param_4; param_3 = param_3 + 1) {
    uVar2 = *param_3;
    if (uVar2 >> 0xb == 0x1b || uVar5 < uVar2) {
      uVar4 = 2;
      goto LAB_00bad8d4;
    }
    bVar3 = (byte)(uVar2 >> 8);
    if (uVar2 >> 0x10 == 0) {
      if (param_7 - (long)param_6 < 2) goto LAB_00bad818;
      pbVar6 = param_6 + 1;
      *param_6 = bVar3;
      lVar7 = 2;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00bad818;
      iVar1 = (uVar2 >> 10 & 0x7c0) + 0x3fc0;
      param_6[2] = bVar3 & 3 | 0xdc;
      *param_6 = (byte)((uint)iVar1 >> 8) | 0xd8;
      lVar7 = 4;
      param_6[1] = (byte)iVar1 | (byte)(uVar2 >> 10) & 0x3f;
      pbVar6 = param_6 + 3;
    }
    *pbVar6 = (byte)uVar2;
    param_6 = param_6 + lVar7;
  }
  uVar4 = 0;
LAB_00bad8d4:
  *param_5 = param_3;
  *param_8 = param_6;
  return uVar4;
}

~~~
