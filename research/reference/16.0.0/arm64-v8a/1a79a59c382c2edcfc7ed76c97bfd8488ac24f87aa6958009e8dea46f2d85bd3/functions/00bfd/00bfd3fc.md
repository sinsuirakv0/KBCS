# 00bfd3fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfd3fc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2edb679b7653a143fe2ae43518559ed7341d4fcca6977818184e20af9c35bb57",
  "source_text_sha256": "2edb679b7653a143fe2ae43518559ed7341d4fcca6977818184e20af9c35bb57"
}
~~~

## 呼び出し元

- [00c5df70](../00c5d/00c5df70.md)

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

## 疑似コード / UTF-8 2139 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc
                 (long *param_1,undefined1 *param_2,long param_3,uint param_4)

{
  long lVar1;
  uint uVar2;
  long *plVar3;
  uint uVar4;
  long lVar5;
  undefined1 *puVar6;
  char local_44 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_44,param_1,1);
  if (local_44[0] != '\0') {
    lVar1 = param_3 + -1;
    if (param_3 < 1) {
      uVar2 = 4;
    }
    else {
      lVar5 = param_1[1];
      if (lVar5 < lVar1) {
        do {
          while( true ) {
            plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
            if ((byte *)plVar3[3] == (byte *)plVar3[4]) {
              uVar2 = (**(code **)(*plVar3 + 0x48))();
              if (uVar2 == 0xffffffff) {
                uVar4 = 2;
                goto LAB_00bfd508;
              }
            }
            else {
              uVar2 = (uint)*(byte *)plVar3[3];
            }
            puVar6 = param_2;
            if ((uVar2 & 0xff) == (param_4 & 0xff)) goto LAB_00bfd504;
            puVar6 = param_2 + 1;
            *param_2 = (char)uVar2;
            lVar5 = 0x7fffffffffffffff;
            if (param_1[1] != 0x7fffffffffffffff) {
              lVar5 = param_1[1] + 1;
              param_1[1] = lVar5;
            }
            plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
            param_2 = puVar6;
            if (plVar3[3] == plVar3[4]) break;
            plVar3[3] = plVar3[3] + 1;
            if (lVar1 <= lVar5) goto LAB_00bfd504;
          }
          (**(code **)(*plVar3 + 0x50))();
        } while (param_1[1] < lVar1);
LAB_00bfd504:
        uVar4 = 0;
        param_2 = puVar6;
LAB_00bfd508:
        lVar5 = param_1[1];
      }
      else {
        uVar4 = 0;
      }
      uVar2 = uVar4 | 4;
      if (lVar5 != 0) {
        uVar2 = uVar4;
      }
      *param_2 = 0;
    }
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar2);
  }
  if (0 < param_3) {
    *param_2 = 0;
  }
  return param_1;
}

~~~
