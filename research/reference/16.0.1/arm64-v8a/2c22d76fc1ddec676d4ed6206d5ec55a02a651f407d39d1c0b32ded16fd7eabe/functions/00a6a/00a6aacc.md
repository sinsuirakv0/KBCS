# 00a6aacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00a6aacc",
  "name": "FUN_00a6aacc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d0e18e762b5468bd0b74beb91041483598c88732d7ff4dfc178ac3b1d381144",
  "source_text_sha256": "9d0e18e762b5468bd0b74beb91041483598c88732d7ff4dfc178ac3b1d381144"
}
~~~

## 呼び出し元

- [0093b770](../0093b/0093b770.md)

## 呼び出し先

- [00a6c0e4](../00a6c/00a6c0e4.md)
- [00a6c110](../00a6c/00a6c110.md)
- [00a6c138](../00a6c/00a6c138.md)
- [00a6c160](../00a6c/00a6c160.md)
- [00a6c1e8](../00a6c/00a6c1e8.md)
- [00a6c488](../00a6c/00a6c488.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1353 bytes

~~~c

void FUN_00a6aacc(undefined8 *param_1,long param_2)

{
  long lVar1;
  long lVar2;
  undefined8 local_50;
  undefined8 uStack_48;
  undefined8 local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  lVar2 = *(long *)(param_2 + 0x70);
  param_1[0xe] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  param_1[1] = 0;
  *param_1 = 0;
  if ((lVar2 != 0) && (lVar2 = FUN_00a6c488(), lVar2 != 0)) {
    FUN_00a6c0e4(&local_50,lVar2);
    param_1[1] = uStack_48;
    *param_1 = local_50;
    param_1[2] = local_40;
    FUN_00a6c110(&local_50,lVar2);
    param_1[4] = uStack_48;
    param_1[3] = local_50;
    param_1[5] = local_40;
    FUN_00a6c138(&local_50,lVar2);
    param_1[7] = uStack_48;
    param_1[6] = local_50;
    param_1[8] = local_40;
    FUN_00a6c160(&local_50,lVar2);
    param_1[10] = uStack_48;
    param_1[9] = local_50;
    param_1[0xb] = local_40;
    FUN_00a6c1e8(&local_50,lVar2);
    param_1[0xd] = uStack_48;
    param_1[0xc] = local_50;
    param_1[0xe] = local_40;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
