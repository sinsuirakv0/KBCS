# 00aed6ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aed6ec",
  "name": "FUN_00aed6ec",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed064d9b1a69d303eab2df5b686470905769f3f9bb8b5a164f21d6e1c3adc411",
  "source_text_sha256": "ed064d9b1a69d303eab2df5b686470905769f3f9bb8b5a164f21d6e1c3adc411"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [008b6efc](../008b6/008b6efc.md)
- [00a46944](../00a46/00a46944.md)
- [00a46c0c](../00a46/00a46c0c.md)

## 疑似コード / UTF-8 1072 bytes

~~~c

void FUN_00aed6ec(long param_1,undefined8 *param_2,int *param_3)

{
  int *piVar1;
  int iVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  iVar2 = *param_3;
  if (iVar2 == 4) {
    lVar5 = *(long *)(param_1 + 8);
    piVar1 = (int *)(lVar5 + 0x846d0);
                    /* try { // try from 00aed74c to 00bed757 has its CatchHandler @ 00aedacc */
    iVar2 = 0;
    if (*piVar1 + 1U < 3) {
      iVar2 = *piVar1 + 1;
    }
    uVar3 = *param_2;
    *(undefined1 *)((long)&fde_table_entry_00335ff0.data_loc + lVar5) = 1;
    *piVar1 = *(int *)(param_1 + (long)iVar2 * 4 + 0x10);
    uVar3 = FUN_008b6efc(uVar3);
    uVar3 = FUN_00a46944(uVar3,0);
    FUN_00a46c0c(uVar3,*piVar1 + 0x86);
    *(undefined1 *)(lVar5 + 0x846d4) = 1;
    return;
  }
  if (iVar2 == 3) {
    uVar3 = FUN_0047ad34();
    uVar4 = 0xb;
  }
  else {
    if (iVar2 != 0) {
      return;
    }
    uVar3 = FUN_0047ad34();
                    /* try { // try from 00aed714 to 00bed71b has its CatchHandler @ 00aedae8 */
    uVar4 = 10;
  }
  FUN_0047ce14(uVar3,uVar4,0);
  return;
}

~~~
