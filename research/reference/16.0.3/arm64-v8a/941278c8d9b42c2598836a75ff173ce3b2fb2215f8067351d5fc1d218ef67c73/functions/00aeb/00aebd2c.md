# 00aebd2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aebd2c",
  "name": "FUN_00aebd2c",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9434a30280d9c0933cad1a670cc1389ae15f9f949169d4c10e5e1baf07b3776a",
  "source_text_sha256": "9434a30280d9c0933cad1a670cc1389ae15f9f949169d4c10e5e1baf07b3776a"
}
~~~

## 呼び出し元

- [007fc1ec](../007fc/007fc1ec.md)
- [0099803c](../00998/0099803c.md)
- [009fe62c](../009fe/009fe62c.md)
- [00a0177c](../00a01/00a0177c.md)
- [00a032d8](../00a03/00a032d8.md)
- [00a04e68](../00a04/00a04e68.md)
- [00ae231c](../00ae2/00ae231c.md)

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [00467e8c](../00467/00467e8c.md)
- [004682b4](../00468/004682b4.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [008524fc](../00852/008524fc.md)
- [00a83a34](../00a83/00a83a34.md)
- [00a845ec](../00a84/00a845ec.md)

## 疑似コード / UTF-8 1310 bytes

~~~c

void FUN_00aebd2c(long param_1,int param_2)

{
  int iVar1;
  int iVar2;
  int iVar3;
  undefined8 uVar4;
  long lVar5;
  
  iVar2 = FUN_00a83a34(param_1 + 0x3078,0x65);
  uVar4 = FUN_00467bc0();
                    /* try { // try from 00aebd60 to 00bebd6b has its CatchHandler @ 00aebecc */
  FUN_008524fc();
  iVar3 = FUN_0046cde4();
                    /* try { // try from 00aebd6c to 00bebe97 has its CatchHandler @ 00aeb974 */
  iVar2 = iVar2 * 0x27;
  lVar5 = FUN_008524fc();
  if (param_2 == 0) {
    iVar1 = iVar2;
    if (iVar2 < 0) {
      iVar1 = iVar2 + 1;
    }
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    param_2 = (((iVar3 >> 1) - (iVar1 >> 1)) -
              *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5)) + 0x12;
  }
  else {
    iVar3 = iVar2 + 0x18;
    if (-0x18 < iVar2) {
      iVar3 = iVar2 + 0x17;
    }
    param_2 = param_2 - (iVar3 >> 1);
  }
  FUN_00467e8c(uVar4,0xff,0xff,0xff,0xe6);
  iVar3 = FUN_0046cd24(param_1);
  FUN_004682b4(uVar4,(int)((double)iVar3 * 0.5 + -430.0),param_2,0x35c,iVar2 + 0x17);
  FUN_00467e8c(uVar4,0,0,0,0xff);
  iVar3 = FUN_0046cd24(param_1);
  if (iVar3 < 0) {
    iVar3 = iVar3 + 1;
  }
  FUN_00a845ec(0x3f800000,param_1 + 0x3078,0x65,iVar3 >> 1,param_2 + 0xd,1);
  FUN_00467e8c(uVar4,0xff,0xff,0xff,0xff);
  return;
}

~~~
