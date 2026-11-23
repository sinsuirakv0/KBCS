# 00bd2aec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bd2a24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2a24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-d6735635ab1d6c367e7bc12b9c2a8abd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd2b30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-b8eef4f7eae7fb70cff19d5c0f66b6e2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2aec",
  "name": "FUN_00bd2aec",
  "size": 916,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cdedf6e4e276e42e7fb722891541d79a871e141f7cf2e8ccea7e4d6cf5ab2b8",
  "source_text_sha256": "2cdedf6e4e276e42e7fb722891541d79a871e141f7cf2e8ccea7e4d6cf5ab2b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2aec",
        "00bd2e7f"
      ]
    ],
    "bytes_sha256": "388533163cff12a062b376e76151148fc97018a165527676af21e984fdbe74ac",
    "instruction_count": 229,
    "instruction_bytes": 916,
    "body_bytes": 916,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc8290](../00bc8/00bc8290.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 関連文字列（未確認候補）

~~~text
" restrict"
" volatile"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6414 bytes

~~~c

void FUN_00bd2aec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  void *pvVar2;
  uint uVar3;
  long lVar4;
  size_t sVar5;
  ulong uVar6;
  long *plVar7;
  
  lVar4 = param_2[1];
  pvVar2 = (void *)*param_2;
                    /* catch() { ... } // from try @ 00bd2ce8 with catch @ 00bd2b0c */
  uVar6 = lVar4 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
  if ((ulong)param_2[2] < uVar6) {
    sVar5 = param_2[2] * 2;
    uVar6 = lVar4 + 0x3e1;
    if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
      sVar5 = uVar6;
    }
    param_2[2] = sVar5;
    pvVar2 = realloc(pvVar2,sVar5);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
    uVar6 = lVar4 + 1;
  }
  param_2[1] = uVar6;
  *(undefined1 *)((long)pvVar2 + lVar4) = 0x28;
  FUN_00bc8290(param_1 + 0x18,param_2);
  lVar4 = param_2[1];
  pvVar2 = (void *)*param_2;
  uVar6 = lVar4 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
  if ((ulong)param_2[2] < uVar6) {
    sVar5 = param_2[2] * 2;
    uVar6 = lVar4 + 0x3e1;
    if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
      sVar5 = uVar6;
    }
    param_2[2] = sVar5;
    pvVar2 = realloc(pvVar2,sVar5);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
    uVar6 = lVar4 + 1;
  }
  param_2[1] = uVar6;
  *(undefined1 *)((long)pvVar2 + lVar4) = 0x29;
  (**(code **)(**(long **)(param_1 + 0x10) + 0x28))(*(long **)(param_1 + 0x10),param_2);
  uVar3 = *(uint *)(param_1 + 0x28);
  if ((uVar3 & 1) != 0) {
    lVar4 = param_2[1];
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 6U) {
      sVar5 = param_2[2] * 2;
      uVar6 = lVar4 + 0x3e6;
      if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
        sVar5 = uVar6;
      }
      param_2[2] = sVar5;
      pvVar2 = realloc(pvVar2,sVar5);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    *(undefined2 *)((undefined4 *)((long)pvVar2 + lVar4) + 1) = 0x7473;
    *(undefined4 *)((long)pvVar2 + lVar4) = 0x6e6f6320;
    uVar3 = *(uint *)(param_1 + 0x28);
    param_2[1] = param_2[1] + 6;
  }
  if ((uVar3 >> 1 & 1) != 0) {
    lVar4 = param_2[1];
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 9U) {
      sVar5 = param_2[2] * 2;
      uVar6 = lVar4 + 0x3e9;
      if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
        sVar5 = uVar6;
      }
      param_2[2] = sVar5;
                    /* try { // try from 00bd2c60 to 00cd2ce7 has its CatchHandler @ 00bd2dcc */
      pvVar2 = realloc(pvVar2,sVar5);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    uVar1 = s_volatile_002ac5f5._0_8_;
    ((char *)((long)pvVar2 + lVar4))[8] = 'e';
    *(undefined8 *)((long)pvVar2 + lVar4) = uVar1;
    uVar3 = *(uint *)(param_1 + 0x28);
    param_2[1] = param_2[1] + 9;
  }
  if ((uVar3 >> 2 & 1) != 0) {
    lVar4 = param_2[1];
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 9U) {
      sVar5 = param_2[2] * 2;
      uVar6 = lVar4 + 0x3e9;
      if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
        sVar5 = uVar6;
      }
      param_2[2] = sVar5;
      pvVar2 = realloc(pvVar2,sVar5);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    uVar1 = s_restrict_002ad79d._0_8_;
                    /* try { // try from 00bd2ce8 to 00cd2e9b has its CatchHandler @ 00bd2b0c */
    ((char *)((long)pvVar2 + lVar4))[8] = 't';
    *(undefined8 *)((long)pvVar2 + lVar4) = uVar1;
    param_2[1] = param_2[1] + 9;
  }
  if (*(char *)(param_1 + 0x2c) == '\x02') {
    lVar4 = param_2[1];
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 3U) {
      sVar5 = param_2[2] * 2;
      uVar6 = lVar4 + 0x3e3;
      if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
        sVar5 = uVar6;
      }
      param_2[2] = sVar5;
      pvVar2 = realloc(pvVar2,sVar5);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    *(undefined1 *)((undefined2 *)((long)pvVar2 + lVar4) + 1) = 0x26;
    *(undefined2 *)((long)pvVar2 + lVar4) = 0x2620;
    lVar4 = 3;
  }
  else {
    if (*(char *)(param_1 + 0x2c) != '\x01') goto LAB_00bd2db8;
    lVar4 = param_2[1];
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 2U) {
      sVar5 = param_2[2] * 2;
      uVar6 = lVar4 + 0x3e2;
      if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
        sVar5 = uVar6;
      }
      param_2[2] = sVar5;
      pvVar2 = realloc(pvVar2,sVar5);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    *(undefined2 *)((long)pvVar2 + lVar4) = 0x2620;
    lVar4 = 2;
  }
  param_2[1] = param_2[1] + lVar4;
LAB_00bd2db8:
  if (*(long *)(param_1 + 0x30) != 0) {
    lVar4 = param_2[1];
    pvVar2 = (void *)*param_2;
    uVar6 = lVar4 + 1;
                    /* catch() { ... } // from try @ 00bd2c60 with catch @ 00bd2dcc */
    if ((ulong)param_2[2] < uVar6) {
      sVar5 = param_2[2] * 2;
      uVar6 = lVar4 + 0x3e1;
      if (sVar5 < uVar6 || sVar5 - uVar6 == 0) {
        sVar5 = uVar6;
      }
      param_2[2] = sVar5;
      pvVar2 = realloc(pvVar2,sVar5);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
      uVar6 = lVar4 + 1;
    }
    param_2[1] = uVar6;
    *(undefined1 *)((long)pvVar2 + lVar4) = 0x20;
    plVar7 = *(long **)(param_1 + 0x30);
    (**(code **)(*plVar7 + 0x20))(plVar7,param_2);
    if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
                    /* WARNING: Could not recover jumptable at 0x00bd2e5c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2aec"></a> `00bd2aec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd2af0"></a> `00bd2af0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd2af4"></a> `00bd2af4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2af8"></a> `00bd2af8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd2afc"></a> `00bd2afc` | `28 a8 40 a9` | ldp x8,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b00"></a> `00bd2b00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd2b04"></a> `00bd2b04` | `2b 20 40 b9` | ldr w11,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2b08"></a> `00bd2b08` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00bd2b0c"></a> `00bd2b0c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd2b10"></a> `00bd2b10` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b14"></a> `00bd2b14` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b18"></a> `00bd2b18` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bd2b1c"></a> `00bd2b1c` | `2b 20 00 b9` | str w11,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2b20"></a> `00bd2b20` | `69 01 00 54` | b.ls 0x00bd2b4c | `CONDITIONAL_JUMP`
<a id="insn-00bd2b24"></a> `00bd2b24` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b28"></a> `00bd2b28` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd2b2c"></a> `00bd2b2c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2b30"></a> `00bd2b30` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2b34"></a> `00bd2b34` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2b38"></a> `00bd2b38` | `b2 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2b3c"></a> `00bd2b3c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2b40"></a> `00bd2b40` | `00 19 00 b4` | cbz x0,0x00bd2e60 | `CONDITIONAL_JUMP`
<a id="insn-00bd2b44"></a> `00bd2b44` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b48"></a> `00bd2b48` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b4c"></a> `00bd2b4c` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b50"></a> `00bd2b50` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00bd2b54"></a> `00bd2b54` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd2b58"></a> `00bd2b58` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd2b5c"></a> `00bd2b5c` | `80 62 00 91` | add x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bd2b60"></a> `00bd2b60` | `cc d5 ff 97` | bl 0x00bc8290 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2b64"></a> `00bd2b64` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b68"></a> `00bd2b68` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2b6c"></a> `00bd2b6c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2b70"></a> `00bd2b70` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b74"></a> `00bd2b74` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b78"></a> `00bd2b78` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2b7c"></a> `00bd2b7c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bd2b80"></a> `00bd2b80` | `69 01 00 54` | b.ls 0x00bd2bac | `CONDITIONAL_JUMP`
<a id="insn-00bd2b84"></a> `00bd2b84` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b88"></a> `00bd2b88` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd2b8c"></a> `00bd2b8c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2b90"></a> `00bd2b90` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2b94"></a> `00bd2b94` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2b98"></a> `00bd2b98` | `9a 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2b9c"></a> `00bd2b9c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2ba0"></a> `00bd2ba0` | `20 16 00 b4` | cbz x0,0x00bd2e64 | `CONDITIONAL_JUMP`
<a id="insn-00bd2ba4"></a> `00bd2ba4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2ba8"></a> `00bd2ba8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2bac"></a> `00bd2bac` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2bb0"></a> `00bd2bb0` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bd2bb4"></a> `00bd2bb4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd2bb8"></a> `00bd2bb8` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd2bbc"></a> `00bd2bbc` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2bc0"></a> `00bd2bc0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd2bc4"></a> `00bd2bc4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd2bc8"></a> `00bd2bc8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd2bcc"></a> `00bd2bcc` | `88 2a 40 b9` | ldr w8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bd2bd0"></a> `00bd2bd0` | `28 03 00 36` | tbz w8,#0x0,0x00bd2c34 | `CONDITIONAL_JUMP`
<a id="insn-00bd2bd4"></a> `00bd2bd4` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2bd8"></a> `00bd2bd8` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2bdc"></a> `00bd2bdc` | `0a 19 00 91` | add x10,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00bd2be0"></a> `00bd2be0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2be4"></a> `00bd2be4` | `49 01 00 54` | b.ls 0x00bd2c0c | `CONDITIONAL_JUMP`
<a id="insn-00bd2be8"></a> `00bd2be8` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2bec"></a> `00bd2bec` | `08 99 0f 91` | add x8,x8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00bd2bf0"></a> `00bd2bf0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2bf4"></a> `00bd2bf4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2bf8"></a> `00bd2bf8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2bfc"></a> `00bd2bfc` | `81 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2c00"></a> `00bd2c00` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2c04"></a> `00bd2c04` | `40 13 00 b4` | cbz x0,0x00bd2e6c | `CONDITIONAL_JUMP`
<a id="insn-00bd2c08"></a> `00bd2c08` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c0c"></a> `00bd2c0c` | `0a 64 8c 52` | mov w10,#0x6320 | `FALL_THROUGH`
<a id="insn-00bd2c10"></a> `00bd2c10` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2c14"></a> `00bd2c14` | `69 8e 8e 52` | mov w9,#0x7473 | `FALL_THROUGH`
<a id="insn-00bd2c18"></a> `00bd2c18` | `ea cd ad 72` | movk w10,#0x6e6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bd2c1c"></a> `00bd2c1c` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bd2c20"></a> `00bd2c20` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bd2c24"></a> `00bd2c24` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c28"></a> `00bd2c28` | `09 19 00 91` | add x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00bd2c2c"></a> `00bd2c2c` | `88 2a 40 b9` | ldr w8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bd2c30"></a> `00bd2c30` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c34"></a> `00bd2c34` | `48 03 08 36` | tbz w8,#0x1,0x00bd2c9c | `CONDITIONAL_JUMP`
<a id="insn-00bd2c38"></a> `00bd2c38` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c3c"></a> `00bd2c3c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2c40"></a> `00bd2c40` | `0a 25 00 91` | add x10,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bd2c44"></a> `00bd2c44` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2c48"></a> `00bd2c48` | `49 01 00 54` | b.ls 0x00bd2c70 | `CONDITIONAL_JUMP`
<a id="insn-00bd2c4c"></a> `00bd2c4c` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2c50"></a> `00bd2c50` | `08 a5 0f 91` | add x8,x8,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bd2c54"></a> `00bd2c54` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2c58"></a> `00bd2c58` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2c5c"></a> `00bd2c5c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2c60"></a> `00bd2c60` | `68 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2c64"></a> `00bd2c64` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2c68"></a> `00bd2c68` | `40 10 00 b4` | cbz x0,0x00bd2e70 | `CONDITIONAL_JUMP`
<a id="insn-00bd2c6c"></a> `00bd2c6c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c70"></a> `00bd2c70` | `c9 b6 ff d0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bd2c74"></a> `00bd2c74` | `29 d5 17 91` | add x9,x9,#0x5f5 | `FALL_THROUGH`
<a id="insn-00bd2c78"></a> `00bd2c78` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2c7c"></a> `00bd2c7c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bd2c80"></a> `00bd2c80` | `aa 0c 80 52` | mov w10,#0x65 | `FALL_THROUGH`
<a id="insn-00bd2c84"></a> `00bd2c84` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c88"></a> `00bd2c88` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bd2c8c"></a> `00bd2c8c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c90"></a> `00bd2c90` | `09 25 00 91` | add x9,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bd2c94"></a> `00bd2c94` | `88 2a 40 b9` | ldr w8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bd2c98"></a> `00bd2c98` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2c9c"></a> `00bd2c9c` | `28 03 10 36` | tbz w8,#0x2,0x00bd2d00 | `CONDITIONAL_JUMP`
<a id="insn-00bd2ca0"></a> `00bd2ca0` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2ca4"></a> `00bd2ca4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2ca8"></a> `00bd2ca8` | `0a 25 00 91` | add x10,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bd2cac"></a> `00bd2cac` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2cb0"></a> `00bd2cb0` | `49 01 00 54` | b.ls 0x00bd2cd8 | `CONDITIONAL_JUMP`
<a id="insn-00bd2cb4"></a> `00bd2cb4` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2cb8"></a> `00bd2cb8` | `08 a5 0f 91` | add x8,x8,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bd2cbc"></a> `00bd2cbc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2cc0"></a> `00bd2cc0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2cc4"></a> `00bd2cc4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2cc8"></a> `00bd2cc8` | `4e 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2ccc"></a> `00bd2ccc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2cd0"></a> `00bd2cd0` | `20 0d 00 b4` | cbz x0,0x00bd2e74 | `CONDITIONAL_JUMP`
<a id="insn-00bd2cd4"></a> `00bd2cd4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2cd8"></a> `00bd2cd8` | `c9 b6 ff f0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bd2cdc"></a> `00bd2cdc` | `29 75 1e 91` | add x9,x9,#0x79d | `FALL_THROUGH`
<a id="insn-00bd2ce0"></a> `00bd2ce0` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2ce4"></a> `00bd2ce4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bd2ce8"></a> `00bd2ce8` | `8a 0e 80 52` | mov w10,#0x74 | `FALL_THROUGH`
<a id="insn-00bd2cec"></a> `00bd2cec` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2cf0"></a> `00bd2cf0` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bd2cf4"></a> `00bd2cf4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2cf8"></a> `00bd2cf8` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bd2cfc"></a> `00bd2cfc` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2d00"></a> `00bd2d00` | `88 b2 40 39` | ldrb w8,[x20, #0x2c] | `FALL_THROUGH`
<a id="insn-00bd2d04"></a> `00bd2d04` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd2d08"></a> `00bd2d08` | `a0 02 00 54` | b.eq 0x00bd2d5c | `CONDITIONAL_JUMP`
<a id="insn-00bd2d0c"></a> `00bd2d0c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2d10"></a> `00bd2d10` | `41 05 00 54` | b.ne 0x00bd2db8 | `CONDITIONAL_JUMP`
<a id="insn-00bd2d14"></a> `00bd2d14` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2d18"></a> `00bd2d18` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2d1c"></a> `00bd2d1c` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd2d20"></a> `00bd2d20` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2d24"></a> `00bd2d24` | `49 01 00 54` | b.ls 0x00bd2d4c | `CONDITIONAL_JUMP`
<a id="insn-00bd2d28"></a> `00bd2d28` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2d2c"></a> `00bd2d2c` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00bd2d30"></a> `00bd2d30` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2d34"></a> `00bd2d34` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2d38"></a> `00bd2d38` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2d3c"></a> `00bd2d3c` | `31 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2d40"></a> `00bd2d40` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2d44"></a> `00bd2d44` | `a0 09 00 b4` | cbz x0,0x00bd2e78 | `CONDITIONAL_JUMP`
<a id="insn-00bd2d48"></a> `00bd2d48` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2d4c"></a> `00bd2d4c` | `09 c4 84 52` | mov w9,#0x2620 | `FALL_THROUGH`
<a id="insn-00bd2d50"></a> `00bd2d50` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bd2d54"></a> `00bd2d54` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd2d58"></a> `00bd2d58` | `15 00 00 14` | b 0x00bd2dac | `UNCONDITIONAL_JUMP`
<a id="insn-00bd2d5c"></a> `00bd2d5c` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2d60"></a> `00bd2d60` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2d64"></a> `00bd2d64` | `0a 0d 00 91` | add x10,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bd2d68"></a> `00bd2d68` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2d6c"></a> `00bd2d6c` | `49 01 00 54` | b.ls 0x00bd2d94 | `CONDITIONAL_JUMP`
<a id="insn-00bd2d70"></a> `00bd2d70` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2d74"></a> `00bd2d74` | `08 8d 0f 91` | add x8,x8,#0x3e3 | `FALL_THROUGH`
<a id="insn-00bd2d78"></a> `00bd2d78` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2d7c"></a> `00bd2d7c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2d80"></a> `00bd2d80` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2d84"></a> `00bd2d84` | `1f 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2d88"></a> `00bd2d88` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2d8c"></a> `00bd2d8c` | `80 07 00 b4` | cbz x0,0x00bd2e7c | `CONDITIONAL_JUMP`
<a id="insn-00bd2d90"></a> `00bd2d90` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2d94"></a> `00bd2d94` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2d98"></a> `00bd2d98` | `c9 04 80 52` | mov w9,#0x26 | `FALL_THROUGH`
<a id="insn-00bd2d9c"></a> `00bd2d9c` | `0a c4 84 52` | mov w10,#0x2620 | `FALL_THROUGH`
<a id="insn-00bd2da0"></a> `00bd2da0` | `09 09 00 39` | strb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bd2da4"></a> `00bd2da4` | `0a 01 00 79` | strh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bd2da8"></a> `00bd2da8` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bd2dac"></a> `00bd2dac` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2db0"></a> `00bd2db0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2db4"></a> `00bd2db4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2db8"></a> `00bd2db8` | `88 1a 40 f9` | ldr x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bd2dbc"></a> `00bd2dbc` | `a8 03 00 b4` | cbz x8,0x00bd2e30 | `CONDITIONAL_JUMP`
<a id="insn-00bd2dc0"></a> `00bd2dc0` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2dc4"></a> `00bd2dc4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2dc8"></a> `00bd2dc8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2dcc"></a> `00bd2dcc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bd2dd0"></a> `00bd2dd0` | `69 01 00 54` | b.ls 0x00bd2dfc | `CONDITIONAL_JUMP`
<a id="insn-00bd2dd4"></a> `00bd2dd4` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2dd8"></a> `00bd2dd8` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd2ddc"></a> `00bd2ddc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2de0"></a> `00bd2de0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2de4"></a> `00bd2de4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2de8"></a> `00bd2de8` | `06 29 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2dec"></a> `00bd2dec` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2df0"></a> `00bd2df0` | `c0 03 00 b4` | cbz x0,0x00bd2e68 | `CONDITIONAL_JUMP`
<a id="insn-00bd2df4"></a> `00bd2df4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2df8"></a> `00bd2df8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2dfc"></a> `00bd2dfc` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2e00"></a> `00bd2e00` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bd2e04"></a> `00bd2e04` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd2e08"></a> `00bd2e08` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd2e0c"></a> `00bd2e0c` | `94 1a 40 f9` | ldr x20,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bd2e10"></a> `00bd2e10` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd2e14"></a> `00bd2e14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd2e18"></a> `00bd2e18` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2e1c"></a> `00bd2e1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd2e20"></a> `00bd2e20` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd2e24"></a> `00bd2e24` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd2e28"></a> `00bd2e28` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd2e2c"></a> `00bd2e2c` | `a1 00 00 54` | b.ne 0x00bd2e40 | `CONDITIONAL_JUMP`
<a id="insn-00bd2e30"></a> `00bd2e30` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2e34"></a> `00bd2e34` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2e38"></a> `00bd2e38` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd2e3c"></a> `00bd2e3c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd2e40"></a> `00bd2e40` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd2e44"></a> `00bd2e44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd2e48"></a> `00bd2e48` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd2e4c"></a> `00bd2e4c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd2e50"></a> `00bd2e50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2e54"></a> `00bd2e54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2e58"></a> `00bd2e58` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd2e5c"></a> `00bd2e5c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bd2e60"></a> `00bd2e60` | `04 2d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e64"></a> `00bd2e64` | `03 2d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e68"></a> `00bd2e68` | `02 2d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e6c"></a> `00bd2e6c` | `01 2d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e70"></a> `00bd2e70` | `00 2d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e74"></a> `00bd2e74` | `ff 2c 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e78"></a> `00bd2e78` | `fe 2c 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd2e7c"></a> `00bd2e7c` | `fd 2c 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2aec`](#insn-00bd2aec) 範囲 `[['00bd2aec', '00bd2b0b']]`
  - `FALL_THROUGH` [`00bd2b08`](#insn-00bd2b08) → [`00bd2b0c`](#insn-00bd2b0c)
- ブロック [`00bd2b0c`](#insn-00bd2b0c) 範囲 `[['00bd2b0c', '00bd2b23']]`
  - `CONDITIONAL_JUMP` [`00bd2b20`](#insn-00bd2b20) → [`00bd2b4c`](#insn-00bd2b4c)
  - `FALL_THROUGH` [`00bd2b20`](#insn-00bd2b20) → [`00bd2b24`](#insn-00bd2b24)
- ブロック [`00bd2b24`](#insn-00bd2b24) 範囲 `[['00bd2b24', '00bd2b43']]`
  - `CONDITIONAL_JUMP` [`00bd2b40`](#insn-00bd2b40) → [`00bd2e60`](#insn-00bd2e60)
  - `FALL_THROUGH` [`00bd2b40`](#insn-00bd2b40) → [`00bd2b44`](#insn-00bd2b44)
- ブロック [`00bd2b44`](#insn-00bd2b44) 範囲 `[['00bd2b44', '00bd2b4b']]`
  - `FALL_THROUGH` [`00bd2b48`](#insn-00bd2b48) → [`00bd2b4c`](#insn-00bd2b4c)
- ブロック [`00bd2b4c`](#insn-00bd2b4c) 範囲 `[['00bd2b4c', '00bd2b83']]`
  - `CONDITIONAL_JUMP` [`00bd2b80`](#insn-00bd2b80) → [`00bd2bac`](#insn-00bd2bac)
  - `FALL_THROUGH` [`00bd2b80`](#insn-00bd2b80) → [`00bd2b84`](#insn-00bd2b84)
- ブロック [`00bd2b84`](#insn-00bd2b84) 範囲 `[['00bd2b84', '00bd2ba3']]`
  - `CONDITIONAL_JUMP` [`00bd2ba0`](#insn-00bd2ba0) → [`00bd2e64`](#insn-00bd2e64)
  - `FALL_THROUGH` [`00bd2ba0`](#insn-00bd2ba0) → [`00bd2ba4`](#insn-00bd2ba4)
- ブロック [`00bd2ba4`](#insn-00bd2ba4) 範囲 `[['00bd2ba4', '00bd2bab']]`
  - `FALL_THROUGH` [`00bd2ba8`](#insn-00bd2ba8) → [`00bd2bac`](#insn-00bd2bac)
- ブロック [`00bd2bac`](#insn-00bd2bac) 範囲 `[['00bd2bac', '00bd2bd3']]`
  - `CONDITIONAL_JUMP` [`00bd2bd0`](#insn-00bd2bd0) → [`00bd2c34`](#insn-00bd2c34)
  - `FALL_THROUGH` [`00bd2bd0`](#insn-00bd2bd0) → [`00bd2bd4`](#insn-00bd2bd4)
- ブロック [`00bd2bd4`](#insn-00bd2bd4) 範囲 `[['00bd2bd4', '00bd2be7']]`
  - `CONDITIONAL_JUMP` [`00bd2be4`](#insn-00bd2be4) → [`00bd2c0c`](#insn-00bd2c0c)
  - `FALL_THROUGH` [`00bd2be4`](#insn-00bd2be4) → [`00bd2be8`](#insn-00bd2be8)
- ブロック [`00bd2be8`](#insn-00bd2be8) 範囲 `[['00bd2be8', '00bd2c07']]`
  - `CONDITIONAL_JUMP` [`00bd2c04`](#insn-00bd2c04) → [`00bd2e6c`](#insn-00bd2e6c)
  - `FALL_THROUGH` [`00bd2c04`](#insn-00bd2c04) → [`00bd2c08`](#insn-00bd2c08)
- ブロック [`00bd2c08`](#insn-00bd2c08) 範囲 `[['00bd2c08', '00bd2c0b']]`
  - `FALL_THROUGH` [`00bd2c08`](#insn-00bd2c08) → [`00bd2c0c`](#insn-00bd2c0c)
- ブロック [`00bd2c0c`](#insn-00bd2c0c) 範囲 `[['00bd2c0c', '00bd2c33']]`
  - `FALL_THROUGH` [`00bd2c30`](#insn-00bd2c30) → [`00bd2c34`](#insn-00bd2c34)
- ブロック [`00bd2c34`](#insn-00bd2c34) 範囲 `[['00bd2c34', '00bd2c37']]`
  - `CONDITIONAL_JUMP` [`00bd2c34`](#insn-00bd2c34) → [`00bd2c9c`](#insn-00bd2c9c)
  - `FALL_THROUGH` [`00bd2c34`](#insn-00bd2c34) → [`00bd2c38`](#insn-00bd2c38)
- ブロック [`00bd2c38`](#insn-00bd2c38) 範囲 `[['00bd2c38', '00bd2c4b']]`
  - `CONDITIONAL_JUMP` [`00bd2c48`](#insn-00bd2c48) → [`00bd2c70`](#insn-00bd2c70)
  - `FALL_THROUGH` [`00bd2c48`](#insn-00bd2c48) → [`00bd2c4c`](#insn-00bd2c4c)
- ブロック [`00bd2c4c`](#insn-00bd2c4c) 範囲 `[['00bd2c4c', '00bd2c5f']]`
  - `FALL_THROUGH` [`00bd2c5c`](#insn-00bd2c5c) → [`00bd2c60`](#insn-00bd2c60)
- ブロック [`00bd2c60`](#insn-00bd2c60) 範囲 `[['00bd2c60', '00bd2c6b']]`
  - `CONDITIONAL_JUMP` [`00bd2c68`](#insn-00bd2c68) → [`00bd2e70`](#insn-00bd2e70)
  - `FALL_THROUGH` [`00bd2c68`](#insn-00bd2c68) → [`00bd2c6c`](#insn-00bd2c6c)
- ブロック [`00bd2c6c`](#insn-00bd2c6c) 範囲 `[['00bd2c6c', '00bd2c6f']]`
  - `FALL_THROUGH` [`00bd2c6c`](#insn-00bd2c6c) → [`00bd2c70`](#insn-00bd2c70)
- ブロック [`00bd2c70`](#insn-00bd2c70) 範囲 `[['00bd2c70', '00bd2c9b']]`
  - `FALL_THROUGH` [`00bd2c98`](#insn-00bd2c98) → [`00bd2c9c`](#insn-00bd2c9c)
- ブロック [`00bd2c9c`](#insn-00bd2c9c) 範囲 `[['00bd2c9c', '00bd2c9f']]`
  - `CONDITIONAL_JUMP` [`00bd2c9c`](#insn-00bd2c9c) → [`00bd2d00`](#insn-00bd2d00)
  - `FALL_THROUGH` [`00bd2c9c`](#insn-00bd2c9c) → [`00bd2ca0`](#insn-00bd2ca0)
- ブロック [`00bd2ca0`](#insn-00bd2ca0) 範囲 `[['00bd2ca0', '00bd2cb3']]`
  - `CONDITIONAL_JUMP` [`00bd2cb0`](#insn-00bd2cb0) → [`00bd2cd8`](#insn-00bd2cd8)
  - `FALL_THROUGH` [`00bd2cb0`](#insn-00bd2cb0) → [`00bd2cb4`](#insn-00bd2cb4)
- ブロック [`00bd2cb4`](#insn-00bd2cb4) 範囲 `[['00bd2cb4', '00bd2cd3']]`
  - `CONDITIONAL_JUMP` [`00bd2cd0`](#insn-00bd2cd0) → [`00bd2e74`](#insn-00bd2e74)
  - `FALL_THROUGH` [`00bd2cd0`](#insn-00bd2cd0) → [`00bd2cd4`](#insn-00bd2cd4)
- ブロック [`00bd2cd4`](#insn-00bd2cd4) 範囲 `[['00bd2cd4', '00bd2cd7']]`
  - `FALL_THROUGH` [`00bd2cd4`](#insn-00bd2cd4) → [`00bd2cd8`](#insn-00bd2cd8)
- ブロック [`00bd2cd8`](#insn-00bd2cd8) 範囲 `[['00bd2cd8', '00bd2ce7']]`
  - `FALL_THROUGH` [`00bd2ce4`](#insn-00bd2ce4) → [`00bd2ce8`](#insn-00bd2ce8)
- ブロック [`00bd2ce8`](#insn-00bd2ce8) 範囲 `[['00bd2ce8', '00bd2cff']]`
  - `FALL_THROUGH` [`00bd2cfc`](#insn-00bd2cfc) → [`00bd2d00`](#insn-00bd2d00)
- ブロック [`00bd2d00`](#insn-00bd2d00) 範囲 `[['00bd2d00', '00bd2d0b']]`
  - `CONDITIONAL_JUMP` [`00bd2d08`](#insn-00bd2d08) → [`00bd2d5c`](#insn-00bd2d5c)
  - `FALL_THROUGH` [`00bd2d08`](#insn-00bd2d08) → [`00bd2d0c`](#insn-00bd2d0c)
- ブロック [`00bd2d0c`](#insn-00bd2d0c) 範囲 `[['00bd2d0c', '00bd2d13']]`
  - `CONDITIONAL_JUMP` [`00bd2d10`](#insn-00bd2d10) → [`00bd2db8`](#insn-00bd2db8)
  - `FALL_THROUGH` [`00bd2d10`](#insn-00bd2d10) → [`00bd2d14`](#insn-00bd2d14)
- ブロック [`00bd2d14`](#insn-00bd2d14) 範囲 `[['00bd2d14', '00bd2d27']]`
  - `CONDITIONAL_JUMP` [`00bd2d24`](#insn-00bd2d24) → [`00bd2d4c`](#insn-00bd2d4c)
  - `FALL_THROUGH` [`00bd2d24`](#insn-00bd2d24) → [`00bd2d28`](#insn-00bd2d28)
- ブロック [`00bd2d28`](#insn-00bd2d28) 範囲 `[['00bd2d28', '00bd2d47']]`
  - `CONDITIONAL_JUMP` [`00bd2d44`](#insn-00bd2d44) → [`00bd2e78`](#insn-00bd2e78)
  - `FALL_THROUGH` [`00bd2d44`](#insn-00bd2d44) → [`00bd2d48`](#insn-00bd2d48)
- ブロック [`00bd2d48`](#insn-00bd2d48) 範囲 `[['00bd2d48', '00bd2d4b']]`
  - `FALL_THROUGH` [`00bd2d48`](#insn-00bd2d48) → [`00bd2d4c`](#insn-00bd2d4c)
- ブロック [`00bd2d4c`](#insn-00bd2d4c) 範囲 `[['00bd2d4c', '00bd2d5b']]`
  - `UNCONDITIONAL_JUMP` [`00bd2d58`](#insn-00bd2d58) → [`00bd2dac`](#insn-00bd2dac)
- ブロック [`00bd2d5c`](#insn-00bd2d5c) 範囲 `[['00bd2d5c', '00bd2d6f']]`
  - `CONDITIONAL_JUMP` [`00bd2d6c`](#insn-00bd2d6c) → [`00bd2d94`](#insn-00bd2d94)
  - `FALL_THROUGH` [`00bd2d6c`](#insn-00bd2d6c) → [`00bd2d70`](#insn-00bd2d70)
- ブロック [`00bd2d70`](#insn-00bd2d70) 範囲 `[['00bd2d70', '00bd2d8f']]`
  - `CONDITIONAL_JUMP` [`00bd2d8c`](#insn-00bd2d8c) → [`00bd2e7c`](#insn-00bd2e7c)
  - `FALL_THROUGH` [`00bd2d8c`](#insn-00bd2d8c) → [`00bd2d90`](#insn-00bd2d90)
- ブロック [`00bd2d90`](#insn-00bd2d90) 範囲 `[['00bd2d90', '00bd2d93']]`
  - `FALL_THROUGH` [`00bd2d90`](#insn-00bd2d90) → [`00bd2d94`](#insn-00bd2d94)
- ブロック [`00bd2d94`](#insn-00bd2d94) 範囲 `[['00bd2d94', '00bd2dab']]`
  - `FALL_THROUGH` [`00bd2da8`](#insn-00bd2da8) → [`00bd2dac`](#insn-00bd2dac)
- ブロック [`00bd2dac`](#insn-00bd2dac) 範囲 `[['00bd2dac', '00bd2db7']]`
  - `FALL_THROUGH` [`00bd2db4`](#insn-00bd2db4) → [`00bd2db8`](#insn-00bd2db8)
- ブロック [`00bd2db8`](#insn-00bd2db8) 範囲 `[['00bd2db8', '00bd2dbf']]`
  - `CONDITIONAL_JUMP` [`00bd2dbc`](#insn-00bd2dbc) → [`00bd2e30`](#insn-00bd2e30)
  - `FALL_THROUGH` [`00bd2dbc`](#insn-00bd2dbc) → [`00bd2dc0`](#insn-00bd2dc0)
- ブロック [`00bd2dc0`](#insn-00bd2dc0) 範囲 `[['00bd2dc0', '00bd2dcb']]`
  - `FALL_THROUGH` [`00bd2dc8`](#insn-00bd2dc8) → [`00bd2dcc`](#insn-00bd2dcc)
- ブロック [`00bd2dcc`](#insn-00bd2dcc) 範囲 `[['00bd2dcc', '00bd2dd3']]`
  - `CONDITIONAL_JUMP` [`00bd2dd0`](#insn-00bd2dd0) → [`00bd2dfc`](#insn-00bd2dfc)
  - `FALL_THROUGH` [`00bd2dd0`](#insn-00bd2dd0) → [`00bd2dd4`](#insn-00bd2dd4)
- ブロック [`00bd2dd4`](#insn-00bd2dd4) 範囲 `[['00bd2dd4', '00bd2df3']]`
  - `CONDITIONAL_JUMP` [`00bd2df0`](#insn-00bd2df0) → [`00bd2e68`](#insn-00bd2e68)
  - `FALL_THROUGH` [`00bd2df0`](#insn-00bd2df0) → [`00bd2df4`](#insn-00bd2df4)
- ブロック [`00bd2df4`](#insn-00bd2df4) 範囲 `[['00bd2df4', '00bd2dfb']]`
  - `FALL_THROUGH` [`00bd2df8`](#insn-00bd2df8) → [`00bd2dfc`](#insn-00bd2dfc)
- ブロック [`00bd2dfc`](#insn-00bd2dfc) 範囲 `[['00bd2dfc', '00bd2e2f']]`
  - `CONDITIONAL_JUMP` [`00bd2e2c`](#insn-00bd2e2c) → [`00bd2e40`](#insn-00bd2e40)
  - `FALL_THROUGH` [`00bd2e2c`](#insn-00bd2e2c) → [`00bd2e30`](#insn-00bd2e30)
- ブロック [`00bd2e30`](#insn-00bd2e30) 範囲 `[['00bd2e30', '00bd2e3f']]`
- ブロック [`00bd2e40`](#insn-00bd2e40) 範囲 `[['00bd2e40', '00bd2e5f']]`
- ブロック [`00bd2e60`](#insn-00bd2e60) 範囲 `[['00bd2e60', '00bd2e63']]`
- ブロック [`00bd2e64`](#insn-00bd2e64) 範囲 `[['00bd2e64', '00bd2e67']]`
- ブロック [`00bd2e68`](#insn-00bd2e68) 範囲 `[['00bd2e68', '00bd2e6b']]`
- ブロック [`00bd2e6c`](#insn-00bd2e6c) 範囲 `[['00bd2e6c', '00bd2e6f']]`
- ブロック [`00bd2e70`](#insn-00bd2e70) 範囲 `[['00bd2e70', '00bd2e73']]`
- ブロック [`00bd2e74`](#insn-00bd2e74) 範囲 `[['00bd2e74', '00bd2e77']]`
- ブロック [`00bd2e78`](#insn-00bd2e78) 範囲 `[['00bd2e78', '00bd2e7b']]`
- ブロック [`00bd2e7c`](#insn-00bd2e7c) 範囲 `[['00bd2e7c', '00bd2e7f']]`

## 命令位置別の参照

- [`00bd2af0`](#insn-00bd2af0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2af4`](#insn-00bd2af4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b20`](#insn-00bd2b20) → [`00bd2b4c`](#insn-00bd2b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b38`](#insn-00bd2b38) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b40`](#insn-00bd2b40) → [`00bd2e60`](#insn-00bd2e60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b60`](#insn-00bd2b60) → [`00bc8290`](../00bc8/00bc8290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc8290` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b80`](#insn-00bd2b80) → [`00bd2bac`](#insn-00bd2bac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b98`](#insn-00bd2b98) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ba0`](#insn-00bd2ba0) → [`00bd2e64`](#insn-00bd2e64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2bd0`](#insn-00bd2bd0) → [`00bd2c34`](#insn-00bd2c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2be4`](#insn-00bd2be4) → [`00bd2c0c`](#insn-00bd2c0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2bfc`](#insn-00bd2bfc) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2c04`](#insn-00bd2c04) → [`00bd2e6c`](#insn-00bd2e6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2c34`](#insn-00bd2c34) → [`00bd2c9c`](#insn-00bd2c9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2c48`](#insn-00bd2c48) → [`00bd2c70`](#insn-00bd2c70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2c60`](#insn-00bd2c60) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2c68`](#insn-00bd2c68) → [`00bd2e70`](#insn-00bd2e70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2c7c`](#insn-00bd2c7c) → `002ac5f5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2c9c`](#insn-00bd2c9c) → [`00bd2d00`](#insn-00bd2d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2cb0`](#insn-00bd2cb0) → [`00bd2cd8`](#insn-00bd2cd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2cc8`](#insn-00bd2cc8) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2cd0`](#insn-00bd2cd0) → [`00bd2e74`](#insn-00bd2e74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ce4`](#insn-00bd2ce4) → `002ad79d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2d08`](#insn-00bd2d08) → [`00bd2d5c`](#insn-00bd2d5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d10`](#insn-00bd2d10) → [`00bd2db8`](#insn-00bd2db8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d24`](#insn-00bd2d24) → [`00bd2d4c`](#insn-00bd2d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d3c`](#insn-00bd2d3c) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d44`](#insn-00bd2d44) → [`00bd2e78`](#insn-00bd2e78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d58`](#insn-00bd2d58) → [`00bd2dac`](#insn-00bd2dac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d6c`](#insn-00bd2d6c) → [`00bd2d94`](#insn-00bd2d94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d84`](#insn-00bd2d84) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2d8c`](#insn-00bd2d8c) → [`00bd2e7c`](#insn-00bd2e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2dbc`](#insn-00bd2dbc) → [`00bd2e30`](#insn-00bd2e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2dd0`](#insn-00bd2dd0) → [`00bd2dfc`](#insn-00bd2dfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2de8`](#insn-00bd2de8) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd2df0`](#insn-00bd2df0) → [`00bd2e68`](#insn-00bd2e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e2c`](#insn-00bd2e2c) → [`00bd2e40`](#insn-00bd2e40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e30`](#insn-00bd2e30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e34`](#insn-00bd2e34) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e50`](#insn-00bd2e50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e54`](#insn-00bd2e54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e60`](#insn-00bd2e60) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e64`](#insn-00bd2e64) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e68`](#insn-00bd2e68) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e6c`](#insn-00bd2e6c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e70`](#insn-00bd2e70) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e74`](#insn-00bd2e74) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e78`](#insn-00bd2e78) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd2e7c`](#insn-00bd2e7c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2af0`](#insn-00bd2af0)

~~~json
{
  "source": "00bd2af0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2af4`](#insn-00bd2af4)

~~~json
{
  "source": "00bd2af4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b20`](#insn-00bd2b20)

~~~json
{
  "source": "00bd2b20",
  "target": "00bd2b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b38`](#insn-00bd2b38)

~~~json
{
  "source": "00bd2b38",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2b40`](#insn-00bd2b40)

~~~json
{
  "source": "00bd2b40",
  "target": "00bd2e60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b60`](#insn-00bd2b60)

~~~json
{
  "source": "00bd2b60",
  "target": "00bc8290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2b80`](#insn-00bd2b80)

~~~json
{
  "source": "00bd2b80",
  "target": "00bd2bac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b98`](#insn-00bd2b98)

~~~json
{
  "source": "00bd2b98",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2ba0`](#insn-00bd2ba0)

~~~json
{
  "source": "00bd2ba0",
  "target": "00bd2e64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2bd0`](#insn-00bd2bd0)

~~~json
{
  "source": "00bd2bd0",
  "target": "00bd2c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2be4`](#insn-00bd2be4)

~~~json
{
  "source": "00bd2be4",
  "target": "00bd2c0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2bfc`](#insn-00bd2bfc)

~~~json
{
  "source": "00bd2bfc",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2c04`](#insn-00bd2c04)

~~~json
{
  "source": "00bd2c04",
  "target": "00bd2e6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2c34`](#insn-00bd2c34)

~~~json
{
  "source": "00bd2c34",
  "target": "00bd2c9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2c48`](#insn-00bd2c48)

~~~json
{
  "source": "00bd2c48",
  "target": "00bd2c70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2c60`](#insn-00bd2c60)

~~~json
{
  "source": "00bd2c60",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2c68`](#insn-00bd2c68)

~~~json
{
  "source": "00bd2c68",
  "target": "00bd2e70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2c7c`](#insn-00bd2c7c)

~~~json
{
  "source": "00bd2c7c",
  "target": "002ac5f5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac5f5",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "20766f6c6174696c6500",
  "capture_start": "002ac5f5",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd2c9c`](#insn-00bd2c9c)

~~~json
{
  "source": "00bd2c9c",
  "target": "00bd2d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2cb0`](#insn-00bd2cb0)

~~~json
{
  "source": "00bd2cb0",
  "target": "00bd2cd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2cc8`](#insn-00bd2cc8)

~~~json
{
  "source": "00bd2cc8",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2cd0`](#insn-00bd2cd0)

~~~json
{
  "source": "00bd2cd0",
  "target": "00bd2e74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ce4`](#insn-00bd2ce4)

~~~json
{
  "source": "00bd2ce4",
  "target": "002ad79d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad79d",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "20726573747269637400",
  "capture_start": "002ad79d",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd2d08`](#insn-00bd2d08)

~~~json
{
  "source": "00bd2d08",
  "target": "00bd2d5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d10`](#insn-00bd2d10)

~~~json
{
  "source": "00bd2d10",
  "target": "00bd2db8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d24`](#insn-00bd2d24)

~~~json
{
  "source": "00bd2d24",
  "target": "00bd2d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d3c`](#insn-00bd2d3c)

~~~json
{
  "source": "00bd2d3c",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2d44`](#insn-00bd2d44)

~~~json
{
  "source": "00bd2d44",
  "target": "00bd2e78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d58`](#insn-00bd2d58)

~~~json
{
  "source": "00bd2d58",
  "target": "00bd2dac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d6c`](#insn-00bd2d6c)

~~~json
{
  "source": "00bd2d6c",
  "target": "00bd2d94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2d84`](#insn-00bd2d84)

~~~json
{
  "source": "00bd2d84",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2d8c`](#insn-00bd2d8c)

~~~json
{
  "source": "00bd2d8c",
  "target": "00bd2e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2dbc`](#insn-00bd2dbc)

~~~json
{
  "source": "00bd2dbc",
  "target": "00bd2e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2dd0`](#insn-00bd2dd0)

~~~json
{
  "source": "00bd2dd0",
  "target": "00bd2dfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2de8`](#insn-00bd2de8)

~~~json
{
  "source": "00bd2de8",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2df0`](#insn-00bd2df0)

~~~json
{
  "source": "00bd2df0",
  "target": "00bd2e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2e2c`](#insn-00bd2e2c)

~~~json
{
  "source": "00bd2e2c",
  "target": "00bd2e40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2e30`](#insn-00bd2e30)

~~~json
{
  "source": "00bd2e30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2e34`](#insn-00bd2e34)

~~~json
{
  "source": "00bd2e34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2e50`](#insn-00bd2e50)

~~~json
{
  "source": "00bd2e50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2e54`](#insn-00bd2e54)

~~~json
{
  "source": "00bd2e54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2e60`](#insn-00bd2e60)

~~~json
{
  "source": "00bd2e60",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e64`](#insn-00bd2e64)

~~~json
{
  "source": "00bd2e64",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e68`](#insn-00bd2e68)

~~~json
{
  "source": "00bd2e68",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e6c`](#insn-00bd2e6c)

~~~json
{
  "source": "00bd2e6c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e70`](#insn-00bd2e70)

~~~json
{
  "source": "00bd2e70",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e74`](#insn-00bd2e74)

~~~json
{
  "source": "00bd2e74",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e78`](#insn-00bd2e78)

~~~json
{
  "source": "00bd2e78",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2e7c`](#insn-00bd2e7c)

~~~json
{
  "source": "00bd2e7c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
