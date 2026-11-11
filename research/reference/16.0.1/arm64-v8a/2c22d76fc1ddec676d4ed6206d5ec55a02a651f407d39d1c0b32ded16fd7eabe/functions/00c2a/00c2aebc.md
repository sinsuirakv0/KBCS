# 00c2aebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c2aebc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6bfbecd6a714d8d78fe954ecc17786f7620c273afe369330f8a1c6d32bcd7297",
  "source_text_sha256": "6bfbecd6a714d8d78fe954ecc17786f7620c273afe369330f8a1c6d32bcd7297"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1370 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,ushort *param_3,ushort *param_4,ulong *param_5,
          undefined2 *param_6,long param_7,undefined8 *param_8)

{
  undefined2 *puVar1;
  ushort uVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  
  uVar4 = *(ulong *)(param_1 + 0x10);
  if ((*(byte *)(param_1 + 0x18) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00c2aed8:
      uVar3 = 1;
      goto LAB_00c2af4c;
    }
    *param_6 = 0xfeff;
    param_6 = param_6 + 1;
  }
  if (param_3 < param_4) {
    lVar5 = param_7 - (long)param_6;
    do {
      uVar2 = *param_3;
      if ((uVar2 & 0xf800) == 0xd800 || uVar4 < uVar2) {
                    /* catch() { ... } // from try @ 00c2b038 with catch @ 00c2af48 */
        uVar3 = 2;
        goto LAB_00c2af4c;
      }
      if (lVar5 < 2) goto LAB_00c2aed8;
      param_3 = param_3 + 1;
      *(char *)param_6 = (char)uVar2;
                    /* catch() { ... } // from try @ 00c2ae8c with catch @ 00c2af20 */
      puVar1 = param_6 + 1;
      *(char *)((long)param_6 + 1) = (char)(uVar2 >> 8);
      param_6 = puVar1;
      lVar5 = lVar5 + -2;
    } while (param_3 < param_4);
    uVar3 = 0;
  }
  else {
    uVar3 = 0;
  }
LAB_00c2af4c:
  *param_5 = (ulong)param_3;
  *param_8 = param_6;
  return uVar3;
}

~~~
