# 00acebcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aceb5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00aceb5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0065.md#compare-5c2b10d5954148e001ef5fff822fe59e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0077.md#compare-70082e895d5d4cb49eadb5f0bc0f5956)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acebcc",
  "name": "FUN_00acebcc",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "030c2731cfc8b82a3d55ebaab2a9d50ed20a08d4e052d1aa88c1b6f5b6f0bc67",
  "source_text_sha256": "030c2731cfc8b82a3d55ebaab2a9d50ed20a08d4e052d1aa88c1b6f5b6f0bc67"
}
~~~

## 呼び出し元

- [005e12e4](../005e1/005e12e4.md)
- [005e1660](../005e1/005e1660.md)
- [005e1790](../005e1/005e1790.md)
- [0066242c](../00662/0066242c.md)
- [006624d0](../00662/006624d0.md)
- [00662574](../00662/00662574.md)
- [007ccf44](../007cc/007ccf44.md)
- [007de918](../007de/007de918.md)
- [008c42e4](../008c4/008c42e4.md)
- [00a421e8](../00a42/00a421e8.md)
- [00a47f54](../00a47/00a47f54.md)
- [00acc640](../00acc/00acc640.md)
- [00ad09c8](../00ad0/00ad09c8.md)
- [00ad6fbc](../00ad6/00ad6fbc.md)
- [00aeb030](../00aeb/00aeb030.md)
- [00aec9fc](../00aec/00aec9fc.md)

## 呼び出し先

- [0067678c](../00676/0067678c.md)
- [007bbda0](../007bb/007bbda0.md)
- [00800244](../00800/00800244.md)
- [00802710](../00802/00802710.md)
- [00802bb0](../00802/00802bb0.md)
- [00802d00](../00802/00802d00.md)
- [00802f38](../00802/00802f38.md)
- [00851550](../00851/00851550.md)
- [00a32a58](../00a32/00a32a58.md)
- [00a32e5c](../00a32/00a32e5c.md)
- [00a32eec](../00a32/00a32eec.md)

## 疑似コード / UTF-8 1332 bytes

~~~c

int FUN_00acebcc(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  ulong uVar5;
  long lVar6;
  undefined8 uVar7;
  
  iVar1 = FUN_00802bb0(0);
  iVar2 = FUN_00802d00();
  iVar3 = FUN_00802f38();
  iVar4 = 1000000000;
  if (iVar3 != 3) {
    iVar4 = 0;
  }
  uVar5 = FUN_00a32a58(param_1 + 0x530,0xffffffff,0xffffffff);
  if ((uVar5 & 1) != 0) {
    iVar1 = FUN_00a32eec(param_1 + 0x530,iVar1);
    return iVar4 + iVar2 + iVar1 * 1000;
  }
  uVar5 = FUN_00a32e5c(param_1 + 0x530);
  if ((uVar5 & 1) == 0) {
                    /* try { // try from 00acec58 to 00bcec8b has its CatchHandler @ 00acf9c0 */
    iVar3 = FUN_00802710(0);
    if (iVar3 == -8) {
      lVar6 = FUN_00851550();
      return *(int *)(lVar6 + 0x33a0);
    }
    uVar5 = FUN_0067678c(param_1 + 0x13d8,1);
    if ((uVar5 & 1) == 0) {
      uVar5 = FUN_007bbda0(param_1,1);
      if ((uVar5 & 1) == 0) goto LAB_00acec44;
      uVar7 = 0x44;
    }
    else {
      uVar7 = 0x2a;
                    /* try { // try from 00acec8c to 00bcec97 has its CatchHandler @ 00acf684 */
    }
    iVar4 = FUN_00800244(0xfffffff8,uVar7);
    iVar4 = iVar4 * 1000;
  }
  else {
LAB_00acec44:
    iVar4 = iVar2 + iVar1 * 1000 + iVar4;
  }
                    /* try { // try from 00acecbc to 00bcecd7 has its CatchHandler @ 00acf958 */
  return iVar4;
}

~~~
