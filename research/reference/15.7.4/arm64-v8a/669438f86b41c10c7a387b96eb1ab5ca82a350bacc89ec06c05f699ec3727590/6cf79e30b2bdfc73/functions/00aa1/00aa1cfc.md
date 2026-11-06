# 00aa1cfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aa1cfc.md)

## 関数情報

~~~json
{
  "address": "00aa1cfc",
  "name": "FUN_00aa1cfc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "def3eb482c3ff3d8002b20609458522705263001015530462cf2f7e6fc34e9f9",
  "source_text_sha256": "def3eb482c3ff3d8002b20609458522705263001015530462cf2f7e6fc34e9f9"
}
~~~
## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00a9f124](../00a9f/00a9f124.md)

## 疑似コード 1/1 / UTF-8 557 bytes

~~~c

int FUN_00aa1cfc(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_0081f580();
  uVar4 = FUN_005c2710(lVar3 + (long)param_1 * 0x1f0 + 0x2678);
  lVar3 = FUN_0081f580();
  if ((uVar4 & 1) == 0) {
    iVar2 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0xa3c0);
  }
  else {
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9eee8);
    iVar2 = FUN_00a9f124(param_1,param_2,param_3,8,0);
    iVar2 = iVar2 + iVar1;
  }
  return iVar2;
}

~~~
