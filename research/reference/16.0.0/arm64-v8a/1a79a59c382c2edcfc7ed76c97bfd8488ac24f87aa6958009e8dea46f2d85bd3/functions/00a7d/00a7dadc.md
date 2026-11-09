# 00a7dadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a7dadc",
  "name": "FUN_00a7dadc",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "65461ea07e741e807c37964e7f2b3f7b3816b099bf39b944c73e71dd9fa937bb",
  "source_text_sha256": "65461ea07e741e807c37964e7f2b3f7b3816b099bf39b944c73e71dd9fa937bb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00b3dfe8](../00b3d/00b3dfe8.md)

## 疑似コード / UTF-8 843 bytes

~~~c

void FUN_00a7dadc(long param_1)

{
  ulong uVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_1 + 8);
  *(undefined4 *)((long)&fde_table_entry_0033e2e0.initial_loc + lVar2) = 0;
  if ((((*(byte *)((long)&DWORD_0042ef40 + lVar2) & 1) == 0) &&
      (*(int *)(&uleb128_0042ef44 + lVar2) == 0)) &&
     (uVar1 = FUN_00b3dfe8(lVar2 + 0x2350,0x47), (uVar1 & 1) != 0)) {
    *(undefined4 *)((long)&QWORD_0039b1b4 + lVar2) = 2;
    *(byte *)((long)&DWORD_0042ef40 + lVar2) = 1;
    *(undefined4 *)(lVar2 + 0x3478) = 0x1c;
  }
  if ((((*(byte *)(lVar2 + 0x16f0) & 1) == 0) && (*(int *)(&uleb128_0042ef44 + lVar2) == 2)) &&
     (uVar1 = FUN_00b3dfe8(lVar2 + 0x2350,0x47), (uVar1 & 1) != 0)) {
    *(undefined1 *)(lVar2 + 0x16f0) = 1;
    *(undefined4 *)((long)&QWORD_0039b1b4 + lVar2) = 2;
    *(undefined4 *)(lVar2 + 0x3478) = 0x26;
  }
  return;
}

~~~
