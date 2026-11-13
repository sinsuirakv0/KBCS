# 00acebcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
