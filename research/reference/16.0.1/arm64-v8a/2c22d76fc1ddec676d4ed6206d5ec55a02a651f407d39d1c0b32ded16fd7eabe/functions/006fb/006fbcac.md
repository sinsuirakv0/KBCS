# 006fbcac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "006fbcac",
  "name": "FUN_006fbcac",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "050b265eda0f381fe7403dcf9bc204d76ddc9893d9032ed43f53900f667bb255",
  "source_text_sha256": "050b265eda0f381fe7403dcf9bc204d76ddc9893d9032ed43f53900f667bb255"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [006b2424](../006b2/006b2424.md)
- [006ea588](../006ea/006ea588.md)
- [006f0500](../006f0/006f0500.md)
- [006fb074](../006fb/006fb074.md)
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)
- [00a83260](../00a83/00a83260.md)

## 疑似コード / UTF-8 1199 bytes

~~~c

void FUN_006fbcac(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined1 *puVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  
  puVar3 = *(undefined1 **)(param_1 + 8);
  if ((*param_3 == 2) && (*param_4 != -1)) {
    uVar4 = *param_2;
    uVar1 = FUN_0047acf4();
    FUN_0047cdd4(uVar1,0xb,0);
    FUN_008b9178(uVar4);
    return;
  }
  if ((*param_3 == 5) && (*param_4 == 0)) {
    *puVar3 = 0;
    puVar5 = (undefined8 *)(puVar3 + 0x28);
    FUN_006fb074(puVar3 + 0x20,*puVar5);
    *(undefined8 **)(puVar3 + 0x20) = puVar5;
    *(undefined8 *)(puVar3 + 0x30) = 0;
    *puVar5 = 0;
    lVar2 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00332070.data_loc + lVar2) = 0;
    lVar2 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00332098.initial_loc + lVar2) = 0;
    lVar2 = FUN_008514f8();
    FUN_00a83260(lVar2 + 0x3078,0x14);
    lVar2 = FUN_008514f8();
    FUN_006b2424(lVar2 + 0x42ef60);
    lVar2 = FUN_008514f8();
    FUN_006f0500(lVar2 + 0x42ef90,*(undefined4 *)(puVar3 + 4),*(undefined4 *)(puVar3 + 0x14));
    lVar2 = FUN_008514f8();
    FUN_006ea588(lVar2 + 0x42ef90,1);
    return;
  }
  return;
}

~~~
