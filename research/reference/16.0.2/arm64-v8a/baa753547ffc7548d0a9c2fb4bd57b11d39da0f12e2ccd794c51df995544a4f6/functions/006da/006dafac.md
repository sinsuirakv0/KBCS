# 006dafac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006dafac",
  "name": "FUN_006dafac",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58e928e0352e724c10a3ef22a3109e3c28755cdd1f24e5794c540594f45d530e",
  "source_text_sha256": "58e928e0352e724c10a3ef22a3109e3c28755cdd1f24e5794c540594f45d530e"
}
~~~

## 呼び出し元

- [006f252c](../006f2/006f252c.md)

## 呼び出し先

- [0046d7f0](../0046d/0046d7f0.md)

## 疑似コード / UTF-8 657 bytes

~~~c

undefined8 FUN_006dafac(int *param_1,int param_2)

{
  int *piVar1;
  int *piVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  
  if ((*(byte *)(param_1 + 0xe) & 1) != 0) {
    return 0;
  }
  piVar1 = *(int **)(param_1 + 8);
  piVar2 = *(int **)(param_1 + 10);
  iVar3 = *param_1;
  *param_1 = iVar3 + param_2;
  while( true ) {
    if (piVar1 == piVar2) {
      return 0;
    }
    if (((iVar3 < *piVar1) && (*piVar1 <= *param_1)) &&
       (iVar4 = piVar1[1], iVar5 = FUN_0046d7f0(1000), iVar5 < iVar4)) break;
    piVar1 = piVar1 + 2;
  }
  *param_1 = 0;
  param_1[4] = param_1[7];
  *(double *)(param_1 + 2) = (double)(param_1[6] * 0x3c);
  return 1;
}

~~~
