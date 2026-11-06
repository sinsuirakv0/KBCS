# 00a3cecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a3cecc.md)

## 関数情報

~~~json
{
  "address": "00a3cecc",
  "name": "FUN_00a3cecc",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3de9573fee8a43d2345f35c2ff5621f1b85cc61b8946fb21906a3ccea7cbf99",
  "source_text_sha256": "e3de9573fee8a43d2345f35c2ff5621f1b85cc61b8946fb21906a3ccea7cbf99"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00469e20](../00469/00469e20.md)
- [0046b908](../0046b/0046b908.md)
- [00646dc4](../00646/00646dc4.md)
- [00a02dd4](../00a02/00a02dd4.md)

## 疑似コード 1/1 / UTF-8 948 bytes

~~~c

void FUN_00a3cecc(long param_1,byte *param_2)

{
  byte *pbVar1;
  ulong uVar2;
  long lVar3;
  
  lVar3 = *(long *)(param_1 + 8);
  if ((*param_2 & 1) == 0) {
    *(undefined1 *)(*(long *)(lVar3 + 0x2180) + 0x20) = 0;
  }
  *(undefined1 *)((long)&QWORD_00397074 + lVar3 + 4) = 0;
  FUN_00469e20();
  FUN_0046b908();
  FUN_00646dc4(0xe);
  pbVar1 = BYTE_ARRAY_0032f921 + lVar3 + 0x13;
  pbVar1[0] = 3;
  pbVar1[1] = 0;
  pbVar1[2] = 0;
  pbVar1[3] = 0;
  *(undefined4 *)(&uleb128_0038b164 + lVar3) = 3;
  *(undefined1 *)(lVar3 + 0x32e9) = 1;
  *(undefined4 *)((long)&QWORD_0032e040 + lVar3) = 0;
  uVar2 = FUN_00a02dd4(lVar3 + 0x22b0);
  if ((uVar2 & 1) != 0) {
    *(undefined4 *)((long)&QWORD_0032e040 + lVar3) = 1;
    BYTE_ARRAY_0033322d[lVar3 + 0x17] = 1;
  }
  *(undefined1 *)((long)&DWORD_0032e038 + lVar3) = 1;
  pbVar1 = BYTE_ARRAY_003c3975 + lVar3 + 0x17;
  pbVar1[0] = 0;
  pbVar1[1] = 0;
  pbVar1[2] = 0;
  pbVar1[3] = 0;
  return;
}

~~~
