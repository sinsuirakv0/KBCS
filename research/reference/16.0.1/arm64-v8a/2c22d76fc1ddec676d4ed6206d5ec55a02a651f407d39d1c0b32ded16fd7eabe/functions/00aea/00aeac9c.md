# 00aeac9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aea874`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0064.md#compare-df907267c75caa588ca9079c791cba2d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0069.md#compare-d245b97f6f94b7cc4c8312e8bad84ce5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeac9c",
  "name": "FUN_00aeac9c",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b081b51717d3e81307e8d611378e6c7d3a88e280f7d5e94f0c078cdf0469a1d6",
  "source_text_sha256": "b081b51717d3e81307e8d611378e6c7d3a88e280f7d5e94f0c078cdf0469a1d6"
}
~~~

## 呼び出し元

- [007fb230](../007fb/007fb230.md)
- [0099703c](../00997/0099703c.md)
- [009fd62c](../009fd/009fd62c.md)
- [00a0077c](../00a00/00a0077c.md)
- [00a022d8](../00a02/00a022d8.md)
- [00a03e68](../00a03/00a03e68.md)
- [00ae128c](../00ae1/00ae128c.md)

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00467b2c](../00467/00467b2c.md)
- [00467f54](../00467/00467f54.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [0046ca84](../0046c/0046ca84.md)
- [008514f8](../00851/008514f8.md)
- [00a829d0](../00a82/00a829d0.md)
- [00a83588](../00a83/00a83588.md)

## 疑似コード / UTF-8 1601 bytes

~~~c

void FUN_00aeac9c(long param_1,int param_2)

{
  int iVar1;
  int iVar2;
  int iVar3;
  undefined8 uVar4;
  long lVar5;
  
                    /* try { // try from 00aeaca8 to 00beacaf has its CatchHandler @ 00aeaec8 */
  iVar2 = FUN_00a829d0(param_1 + 0x3078,0x65);
  uVar4 = FUN_00467860();
  FUN_008514f8();
  iVar3 = FUN_0046ca84();
  iVar2 = iVar2 * 0x27;
  lVar5 = FUN_008514f8();
  if (param_2 == 0) {
    iVar1 = iVar2;
    if (iVar2 < 0) {
      iVar1 = iVar2 + 1;
    }
                    /* try { // try from 00aead14 to 00bead1b has its CatchHandler @ 00aeaec4 */
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    param_2 = (((iVar3 >> 1) - (iVar1 >> 1)) -
              *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5)) + 0x12;
  }
  else {
                    /* try { // try from 00aeacf4 to 00beacff has its CatchHandler @ 00aeaed4 */
    iVar3 = iVar2 + 0x18;
    if (-0x18 < iVar2) {
      iVar3 = iVar2 + 0x17;
    }
    param_2 = param_2 - (iVar3 >> 1);
  }
  FUN_00467b2c(uVar4,0xff,0xff,0xff,0xe6);
  iVar3 = FUN_0046c9c4(param_1);
                    /* try { // try from 00aead60 to 00bead6b has its CatchHandler @ 00aeaecc */
                    /* try { // try from 00aead6c to 00beae97 has its CatchHandler @ 00aea974 */
  FUN_00467f54(uVar4,(int)((double)iVar3 * 0.5 + -430.0),param_2,0x35c,iVar2 + 0x17);
  FUN_00467b2c(uVar4,0,0,0,0xff);
  iVar3 = FUN_0046c9c4(param_1);
  if (iVar3 < 0) {
    iVar3 = iVar3 + 1;
  }
  FUN_00a83588(0x3f800000,param_1 + 0x3078,0x65,iVar3 >> 1,param_2 + 0xd,1);
  FUN_00467b2c(uVar4,0xff,0xff,0xff,0xff);
  return;
}

~~~
