# 00ad9efc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad9eb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9eb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-4b44558c8af01be365c5f9ece316ca0d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0090.md#review-686ecdca9c2f8c2ffc02a4f5fad29297)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad9efc",
  "name": "FUN_00ad9efc",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88452dd1eea19638c9f26b352c68bf35a82f262c8eccd2b158e369859ed6652c",
  "source_text_sha256": "88452dd1eea19638c9f26b352c68bf35a82f262c8eccd2b158e369859ed6652c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad9efc",
        "00ada093"
      ]
    ],
    "bytes_sha256": "c4ae077bf0b2ed780bbc1255d97bab529d3cd916034f58355f4f6d6ed1f14a06",
    "instruction_count": 102,
    "instruction_bytes": 408,
    "body_bytes": 408,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00ad9b64](../00ad9/00ad9b64.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2499 bytes

~~~c

long * FUN_00ad9efc(long *param_1,long param_2)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  
  plVar3 = param_1 + 4;
                    /* catch() { ... } // from try @ 00ad9be0 with catch @ 00ad9f14 */
                    /* catch() { ... } // from try @ 00ad9adc with catch @ 00ad9f18 */
  plVar1 = (long *)*plVar3;
                    /* catch() { ... } // from try @ 00ad9d9c with catch @ 00ad9f1c */
  *plVar3 = 0;
                    /* catch() { ... } // from try @ 00ad9dac with catch @ 00ad9f24 */
  if (plVar1 == param_1) {
    lVar2 = 0x20;
    plVar1 = param_1;
LAB_00ad9f3c:
    (**(code **)(*plVar1 + lVar2))();
  }
  else {
                    /* catch() { ... } // from try @ 00ad9df4 with catch @ 00ad9f28 */
    if (plVar1 != (long *)0x0) {
      lVar2 = 0x28;
                    /* catch() { ... } // from try @ 00ad9e04 with catch @ 00ad9f30 */
      goto LAB_00ad9f3c;
    }
  }
  plVar1 = (long *)(param_2 + 0x20);
  lVar2 = *plVar1;
  if (lVar2 == 0) {
LAB_00ad9f68:
    *plVar3 = 0;
  }
  else {
    if (lVar2 != param_2) {
      *plVar3 = lVar2;
      plVar3 = plVar1;
      goto LAB_00ad9f68;
    }
    param_1[4] = (long)param_1;
    (**(code **)(*(long *)*plVar1 + 0x18))((long *)*plVar1,param_1);
  }
  plVar3 = param_1 + 10;
  plVar1 = (long *)*plVar3;
  plVar4 = param_1 + 6;
  *plVar3 = 0;
  if (plVar1 == plVar4) {
    lVar2 = 0x20;
    plVar1 = plVar4;
LAB_00ad9fb4:
    (**(code **)(*plVar1 + lVar2))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar2 = 0x28;
    goto LAB_00ad9fb4;
  }
  plVar1 = (long *)(param_2 + 0x50);
  lVar2 = *plVar1;
  if (lVar2 == 0) {
LAB_00ad9fe4:
    *plVar3 = 0;
  }
  else {
    if (lVar2 != param_2 + 0x30) {
      *plVar3 = lVar2;
      plVar3 = plVar1;
      goto LAB_00ad9fe4;
    }
    *plVar3 = (long)plVar4;
    (**(code **)(*(long *)*plVar1 + 0x18))((long *)*plVar1,plVar4);
  }
  plVar3 = param_1 + 0x10;
  plVar1 = (long *)*plVar3;
  plVar4 = param_1 + 0xc;
  *plVar3 = 0;
  if (plVar1 == plVar4) {
    lVar2 = 0x20;
    plVar1 = plVar4;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_00ada03c;
    lVar2 = 0x28;
  }
  (**(code **)(*plVar1 + lVar2))();
LAB_00ada03c:
  plVar1 = (long *)(param_2 + 0x80);
  lVar2 = *plVar1;
  if (lVar2 != 0) {
    if (lVar2 == param_2 + 0x60) {
      *plVar3 = (long)plVar4;
      (**(code **)(*(long *)*plVar1 + 0x18))((long *)*plVar1,plVar4);
      return param_1;
    }
    *plVar3 = lVar2;
    plVar3 = plVar1;
  }
  *plVar3 = 0;
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad9efc"></a> `00ad9efc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ad9f00"></a> `00ad9f00` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad9f04"></a> `00ad9f04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad9f08"></a> `00ad9f08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ad9f0c"></a> `00ad9f0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ad9f10"></a> `00ad9f10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ad9f14"></a> `00ad9f14` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ad9f18"></a> `00ad9f18` | `a0 0e 42 f8` | ldr x0,[x21, #0x20]! | `FALL_THROUGH`
<a id="insn-00ad9f1c"></a> `00ad9f1c` | `bf 02 00 f9` | str xzr,[x21] | `FALL_THROUGH`
<a id="insn-00ad9f20"></a> `00ad9f20` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-00ad9f24"></a> `00ad9f24` | `80 00 00 54` | b.eq 0x00ad9f34 | `CONDITIONAL_JUMP`
<a id="insn-00ad9f28"></a> `00ad9f28` | `00 01 00 b4` | cbz x0,0x00ad9f48 | `CONDITIONAL_JUMP`
<a id="insn-00ad9f2c"></a> `00ad9f2c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad9f30"></a> `00ad9f30` | `03 00 00 14` | b 0x00ad9f3c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad9f34"></a> `00ad9f34` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad9f38"></a> `00ad9f38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad9f3c"></a> `00ad9f3c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ad9f40"></a> `00ad9f40` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad9f44"></a> `00ad9f44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad9f48"></a> `00ad9f48` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00ad9f4c"></a> `00ad9f4c` | `09 0d 42 f8` | ldr x9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ad9f50"></a> `00ad9f50` | `a9 00 00 b4` | cbz x9,0x00ad9f64 | `CONDITIONAL_JUMP`
<a id="insn-00ad9f54"></a> `00ad9f54` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00ad9f58"></a> `00ad9f58` | `c0 00 00 54` | b.eq 0x00ad9f70 | `CONDITIONAL_JUMP`
<a id="insn-00ad9f5c"></a> `00ad9f5c` | `a9 02 00 f9` | str x9,[x21] | `FALL_THROUGH`
<a id="insn-00ad9f60"></a> `00ad9f60` | `02 00 00 14` | b 0x00ad9f68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad9f64"></a> `00ad9f64` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00ad9f68"></a> `00ad9f68` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00ad9f6c"></a> `00ad9f6c` | `07 00 00 14` | b 0x00ad9f88 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad9f70"></a> `00ad9f70` | `73 12 00 f9` | str x19,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00ad9f74"></a> `00ad9f74` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00ad9f78"></a> `00ad9f78` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad9f7c"></a> `00ad9f7c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00ad9f80"></a> `00ad9f80` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00ad9f84"></a> `00ad9f84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad9f88"></a> `00ad9f88` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00ad9f8c"></a> `00ad9f8c` | `c0 0e 45 f8` | ldr x0,[x22, #0x50]! | `FALL_THROUGH`
<a id="insn-00ad9f90"></a> `00ad9f90` | `d5 82 00 d1` | sub x21,x22,#0x20 | `FALL_THROUGH`
<a id="insn-00ad9f94"></a> `00ad9f94` | `df 02 00 f9` | str xzr,[x22] | `FALL_THROUGH`
<a id="insn-00ad9f98"></a> `00ad9f98` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00ad9f9c"></a> `00ad9f9c` | `80 00 00 54` | b.eq 0x00ad9fac | `CONDITIONAL_JUMP`
<a id="insn-00ad9fa0"></a> `00ad9fa0` | `00 01 00 b4` | cbz x0,0x00ad9fc0 | `CONDITIONAL_JUMP`
<a id="insn-00ad9fa4"></a> `00ad9fa4` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad9fa8"></a> `00ad9fa8` | `03 00 00 14` | b 0x00ad9fb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad9fac"></a> `00ad9fac` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad9fb0"></a> `00ad9fb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad9fb4"></a> `00ad9fb4` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ad9fb8"></a> `00ad9fb8` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad9fbc"></a> `00ad9fbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad9fc0"></a> `00ad9fc0` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00ad9fc4"></a> `00ad9fc4` | `09 0d 45 f8` | ldr x9,[x8, #0x50]! | `FALL_THROUGH`
<a id="insn-00ad9fc8"></a> `00ad9fc8` | `c9 00 00 b4` | cbz x9,0x00ad9fe0 | `CONDITIONAL_JUMP`
<a id="insn-00ad9fcc"></a> `00ad9fcc` | `8a c2 00 91` | add x10,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00ad9fd0"></a> `00ad9fd0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00ad9fd4"></a> `00ad9fd4` | `c0 00 00 54` | b.eq 0x00ad9fec | `CONDITIONAL_JUMP`
<a id="insn-00ad9fd8"></a> `00ad9fd8` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00ad9fdc"></a> `00ad9fdc` | `02 00 00 14` | b 0x00ad9fe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad9fe0"></a> `00ad9fe0` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ad9fe4"></a> `00ad9fe4` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00ad9fe8"></a> `00ad9fe8` | `07 00 00 14` | b 0x00ada004 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad9fec"></a> `00ad9fec` | `d5 02 00 f9` | str x21,[x22] | `FALL_THROUGH`
<a id="insn-00ad9ff0"></a> `00ad9ff0` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00ad9ff4"></a> `00ad9ff4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad9ff8"></a> `00ad9ff8` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00ad9ffc"></a> `00ad9ffc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ada000"></a> `00ada000` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada004"></a> `00ada004` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00ada008"></a> `00ada008` | `c0 0e 48 f8` | ldr x0,[x22, #0x80]! | `FALL_THROUGH`
<a id="insn-00ada00c"></a> `00ada00c` | `d5 82 00 d1` | sub x21,x22,#0x20 | `FALL_THROUGH`
<a id="insn-00ada010"></a> `00ada010` | `df 02 00 f9` | str xzr,[x22] | `FALL_THROUGH`
<a id="insn-00ada014"></a> `00ada014` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00ada018"></a> `00ada018` | `80 00 00 54` | b.eq 0x00ada028 | `CONDITIONAL_JUMP`
<a id="insn-00ada01c"></a> `00ada01c` | `00 01 00 b4` | cbz x0,0x00ada03c | `CONDITIONAL_JUMP`
<a id="insn-00ada020"></a> `00ada020` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ada024"></a> `00ada024` | `03 00 00 14` | b 0x00ada030 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada028"></a> `00ada028` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ada02c"></a> `00ada02c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ada030"></a> `00ada030` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ada034"></a> `00ada034` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ada038"></a> `00ada038` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada03c"></a> `00ada03c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00ada040"></a> `00ada040` | `09 0d 48 f8` | ldr x9,[x8, #0x80]! | `FALL_THROUGH`
<a id="insn-00ada044"></a> `00ada044` | `c9 00 00 b4` | cbz x9,0x00ada05c | `CONDITIONAL_JUMP`
<a id="insn-00ada048"></a> `00ada048` | `8a 82 01 91` | add x10,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00ada04c"></a> `00ada04c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00ada050"></a> `00ada050` | `c0 00 00 54` | b.eq 0x00ada068 | `CONDITIONAL_JUMP`
<a id="insn-00ada054"></a> `00ada054` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00ada058"></a> `00ada058` | `02 00 00 14` | b 0x00ada060 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada05c"></a> `00ada05c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ada060"></a> `00ada060` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00ada064"></a> `00ada064` | `07 00 00 14` | b 0x00ada080 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada068"></a> `00ada068` | `d5 02 00 f9` | str x21,[x22] | `FALL_THROUGH`
<a id="insn-00ada06c"></a> `00ada06c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00ada070"></a> `00ada070` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ada074"></a> `00ada074` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00ada078"></a> `00ada078` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ada07c"></a> `00ada07c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada080"></a> `00ada080` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ada084"></a> `00ada084` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ada088"></a> `00ada088` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ada08c"></a> `00ada08c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ada090"></a> `00ada090` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad9efc`](#insn-00ad9efc) 範囲 `[['00ad9efc', '00ad9f13']]`
  - `FALL_THROUGH` [`00ad9f10`](#insn-00ad9f10) → [`00ad9f14`](#insn-00ad9f14)
- ブロック [`00ad9f14`](#insn-00ad9f14) 範囲 `[['00ad9f14', '00ad9f17']]`
  - `FALL_THROUGH` [`00ad9f14`](#insn-00ad9f14) → [`00ad9f18`](#insn-00ad9f18)
- ブロック [`00ad9f18`](#insn-00ad9f18) 範囲 `[['00ad9f18', '00ad9f1b']]`
  - `FALL_THROUGH` [`00ad9f18`](#insn-00ad9f18) → [`00ad9f1c`](#insn-00ad9f1c)
- ブロック [`00ad9f1c`](#insn-00ad9f1c) 範囲 `[['00ad9f1c', '00ad9f23']]`
  - `FALL_THROUGH` [`00ad9f20`](#insn-00ad9f20) → [`00ad9f24`](#insn-00ad9f24)
- ブロック [`00ad9f24`](#insn-00ad9f24) 範囲 `[['00ad9f24', '00ad9f27']]`
  - `CONDITIONAL_JUMP` [`00ad9f24`](#insn-00ad9f24) → [`00ad9f34`](#insn-00ad9f34)
  - `FALL_THROUGH` [`00ad9f24`](#insn-00ad9f24) → [`00ad9f28`](#insn-00ad9f28)
- ブロック [`00ad9f28`](#insn-00ad9f28) 範囲 `[['00ad9f28', '00ad9f2b']]`
  - `CONDITIONAL_JUMP` [`00ad9f28`](#insn-00ad9f28) → [`00ad9f48`](#insn-00ad9f48)
  - `FALL_THROUGH` [`00ad9f28`](#insn-00ad9f28) → [`00ad9f2c`](#insn-00ad9f2c)
- ブロック [`00ad9f2c`](#insn-00ad9f2c) 範囲 `[['00ad9f2c', '00ad9f2f']]`
  - `FALL_THROUGH` [`00ad9f2c`](#insn-00ad9f2c) → [`00ad9f30`](#insn-00ad9f30)
- ブロック [`00ad9f30`](#insn-00ad9f30) 範囲 `[['00ad9f30', '00ad9f33']]`
  - `UNCONDITIONAL_JUMP` [`00ad9f30`](#insn-00ad9f30) → [`00ad9f3c`](#insn-00ad9f3c)
- ブロック [`00ad9f34`](#insn-00ad9f34) 範囲 `[['00ad9f34', '00ad9f3b']]`
  - `FALL_THROUGH` [`00ad9f38`](#insn-00ad9f38) → [`00ad9f3c`](#insn-00ad9f3c)
- ブロック [`00ad9f3c`](#insn-00ad9f3c) 範囲 `[['00ad9f3c', '00ad9f47']]`
  - `FALL_THROUGH` [`00ad9f44`](#insn-00ad9f44) → [`00ad9f48`](#insn-00ad9f48)
- ブロック [`00ad9f48`](#insn-00ad9f48) 範囲 `[['00ad9f48', '00ad9f53']]`
  - `CONDITIONAL_JUMP` [`00ad9f50`](#insn-00ad9f50) → [`00ad9f64`](#insn-00ad9f64)
  - `FALL_THROUGH` [`00ad9f50`](#insn-00ad9f50) → [`00ad9f54`](#insn-00ad9f54)
- ブロック [`00ad9f54`](#insn-00ad9f54) 範囲 `[['00ad9f54', '00ad9f5b']]`
  - `CONDITIONAL_JUMP` [`00ad9f58`](#insn-00ad9f58) → [`00ad9f70`](#insn-00ad9f70)
  - `FALL_THROUGH` [`00ad9f58`](#insn-00ad9f58) → [`00ad9f5c`](#insn-00ad9f5c)
- ブロック [`00ad9f5c`](#insn-00ad9f5c) 範囲 `[['00ad9f5c', '00ad9f63']]`
  - `UNCONDITIONAL_JUMP` [`00ad9f60`](#insn-00ad9f60) → [`00ad9f68`](#insn-00ad9f68)
- ブロック [`00ad9f64`](#insn-00ad9f64) 範囲 `[['00ad9f64', '00ad9f67']]`
  - `FALL_THROUGH` [`00ad9f64`](#insn-00ad9f64) → [`00ad9f68`](#insn-00ad9f68)
- ブロック [`00ad9f68`](#insn-00ad9f68) 範囲 `[['00ad9f68', '00ad9f6f']]`
  - `UNCONDITIONAL_JUMP` [`00ad9f6c`](#insn-00ad9f6c) → [`00ad9f88`](#insn-00ad9f88)
- ブロック [`00ad9f70`](#insn-00ad9f70) 範囲 `[['00ad9f70', '00ad9f87']]`
  - `FALL_THROUGH` [`00ad9f84`](#insn-00ad9f84) → [`00ad9f88`](#insn-00ad9f88)
- ブロック [`00ad9f88`](#insn-00ad9f88) 範囲 `[['00ad9f88', '00ad9f9f']]`
  - `CONDITIONAL_JUMP` [`00ad9f9c`](#insn-00ad9f9c) → [`00ad9fac`](#insn-00ad9fac)
  - `FALL_THROUGH` [`00ad9f9c`](#insn-00ad9f9c) → [`00ad9fa0`](#insn-00ad9fa0)
- ブロック [`00ad9fa0`](#insn-00ad9fa0) 範囲 `[['00ad9fa0', '00ad9fa3']]`
  - `CONDITIONAL_JUMP` [`00ad9fa0`](#insn-00ad9fa0) → [`00ad9fc0`](#insn-00ad9fc0)
  - `FALL_THROUGH` [`00ad9fa0`](#insn-00ad9fa0) → [`00ad9fa4`](#insn-00ad9fa4)
- ブロック [`00ad9fa4`](#insn-00ad9fa4) 範囲 `[['00ad9fa4', '00ad9fab']]`
  - `UNCONDITIONAL_JUMP` [`00ad9fa8`](#insn-00ad9fa8) → [`00ad9fb4`](#insn-00ad9fb4)
- ブロック [`00ad9fac`](#insn-00ad9fac) 範囲 `[['00ad9fac', '00ad9fb3']]`
  - `FALL_THROUGH` [`00ad9fb0`](#insn-00ad9fb0) → [`00ad9fb4`](#insn-00ad9fb4)
- ブロック [`00ad9fb4`](#insn-00ad9fb4) 範囲 `[['00ad9fb4', '00ad9fbf']]`
  - `FALL_THROUGH` [`00ad9fbc`](#insn-00ad9fbc) → [`00ad9fc0`](#insn-00ad9fc0)
- ブロック [`00ad9fc0`](#insn-00ad9fc0) 範囲 `[['00ad9fc0', '00ad9fcb']]`
  - `CONDITIONAL_JUMP` [`00ad9fc8`](#insn-00ad9fc8) → [`00ad9fe0`](#insn-00ad9fe0)
  - `FALL_THROUGH` [`00ad9fc8`](#insn-00ad9fc8) → [`00ad9fcc`](#insn-00ad9fcc)
- ブロック [`00ad9fcc`](#insn-00ad9fcc) 範囲 `[['00ad9fcc', '00ad9fd7']]`
  - `CONDITIONAL_JUMP` [`00ad9fd4`](#insn-00ad9fd4) → [`00ad9fec`](#insn-00ad9fec)
  - `FALL_THROUGH` [`00ad9fd4`](#insn-00ad9fd4) → [`00ad9fd8`](#insn-00ad9fd8)
- ブロック [`00ad9fd8`](#insn-00ad9fd8) 範囲 `[['00ad9fd8', '00ad9fdf']]`
  - `UNCONDITIONAL_JUMP` [`00ad9fdc`](#insn-00ad9fdc) → [`00ad9fe4`](#insn-00ad9fe4)
- ブロック [`00ad9fe0`](#insn-00ad9fe0) 範囲 `[['00ad9fe0', '00ad9fe3']]`
  - `FALL_THROUGH` [`00ad9fe0`](#insn-00ad9fe0) → [`00ad9fe4`](#insn-00ad9fe4)
- ブロック [`00ad9fe4`](#insn-00ad9fe4) 範囲 `[['00ad9fe4', '00ad9feb']]`
  - `UNCONDITIONAL_JUMP` [`00ad9fe8`](#insn-00ad9fe8) → [`00ada004`](#insn-00ada004)
- ブロック [`00ad9fec`](#insn-00ad9fec) 範囲 `[['00ad9fec', '00ada003']]`
  - `FALL_THROUGH` [`00ada000`](#insn-00ada000) → [`00ada004`](#insn-00ada004)
- ブロック [`00ada004`](#insn-00ada004) 範囲 `[['00ada004', '00ada01b']]`
  - `CONDITIONAL_JUMP` [`00ada018`](#insn-00ada018) → [`00ada028`](#insn-00ada028)
  - `FALL_THROUGH` [`00ada018`](#insn-00ada018) → [`00ada01c`](#insn-00ada01c)
- ブロック [`00ada01c`](#insn-00ada01c) 範囲 `[['00ada01c', '00ada01f']]`
  - `CONDITIONAL_JUMP` [`00ada01c`](#insn-00ada01c) → [`00ada03c`](#insn-00ada03c)
  - `FALL_THROUGH` [`00ada01c`](#insn-00ada01c) → [`00ada020`](#insn-00ada020)
- ブロック [`00ada020`](#insn-00ada020) 範囲 `[['00ada020', '00ada027']]`
  - `UNCONDITIONAL_JUMP` [`00ada024`](#insn-00ada024) → [`00ada030`](#insn-00ada030)
- ブロック [`00ada028`](#insn-00ada028) 範囲 `[['00ada028', '00ada02f']]`
  - `FALL_THROUGH` [`00ada02c`](#insn-00ada02c) → [`00ada030`](#insn-00ada030)
- ブロック [`00ada030`](#insn-00ada030) 範囲 `[['00ada030', '00ada03b']]`
  - `FALL_THROUGH` [`00ada038`](#insn-00ada038) → [`00ada03c`](#insn-00ada03c)
- ブロック [`00ada03c`](#insn-00ada03c) 範囲 `[['00ada03c', '00ada047']]`
  - `CONDITIONAL_JUMP` [`00ada044`](#insn-00ada044) → [`00ada05c`](#insn-00ada05c)
  - `FALL_THROUGH` [`00ada044`](#insn-00ada044) → [`00ada048`](#insn-00ada048)
- ブロック [`00ada048`](#insn-00ada048) 範囲 `[['00ada048', '00ada053']]`
  - `CONDITIONAL_JUMP` [`00ada050`](#insn-00ada050) → [`00ada068`](#insn-00ada068)
  - `FALL_THROUGH` [`00ada050`](#insn-00ada050) → [`00ada054`](#insn-00ada054)
- ブロック [`00ada054`](#insn-00ada054) 範囲 `[['00ada054', '00ada05b']]`
  - `UNCONDITIONAL_JUMP` [`00ada058`](#insn-00ada058) → [`00ada060`](#insn-00ada060)
- ブロック [`00ada05c`](#insn-00ada05c) 範囲 `[['00ada05c', '00ada05f']]`
  - `FALL_THROUGH` [`00ada05c`](#insn-00ada05c) → [`00ada060`](#insn-00ada060)
- ブロック [`00ada060`](#insn-00ada060) 範囲 `[['00ada060', '00ada067']]`
  - `UNCONDITIONAL_JUMP` [`00ada064`](#insn-00ada064) → [`00ada080`](#insn-00ada080)
- ブロック [`00ada068`](#insn-00ada068) 範囲 `[['00ada068', '00ada07f']]`
  - `FALL_THROUGH` [`00ada07c`](#insn-00ada07c) → [`00ada080`](#insn-00ada080)
- ブロック [`00ada080`](#insn-00ada080) 範囲 `[['00ada080', '00ada093']]`

## 命令位置別の参照

- [`00ad9efc`](#insn-00ad9efc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f00`](#insn-00ad9f00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f04`](#insn-00ad9f04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f24`](#insn-00ad9f24) → [`00ad9f34`](#insn-00ad9f34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f28`](#insn-00ad9f28) → [`00ad9f48`](#insn-00ad9f48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f30`](#insn-00ad9f30) → [`00ad9f3c`](#insn-00ad9f3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f50`](#insn-00ad9f50) → [`00ad9f64`](#insn-00ad9f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f58`](#insn-00ad9f58) → [`00ad9f70`](#insn-00ad9f70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f60`](#insn-00ad9f60) → [`00ad9f68`](#insn-00ad9f68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f6c`](#insn-00ad9f6c) → [`00ad9f88`](#insn-00ad9f88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9f9c`](#insn-00ad9f9c) → [`00ad9fac`](#insn-00ad9fac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9fa0`](#insn-00ad9fa0) → [`00ad9fc0`](#insn-00ad9fc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9fa8`](#insn-00ad9fa8) → [`00ad9fb4`](#insn-00ad9fb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9fc8`](#insn-00ad9fc8) → [`00ad9fe0`](#insn-00ad9fe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9fd4`](#insn-00ad9fd4) → [`00ad9fec`](#insn-00ad9fec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9fdc`](#insn-00ad9fdc) → [`00ad9fe4`](#insn-00ad9fe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad9fe8`](#insn-00ad9fe8) → [`00ada004`](#insn-00ada004) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada018`](#insn-00ada018) → [`00ada028`](#insn-00ada028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada01c`](#insn-00ada01c) → [`00ada03c`](#insn-00ada03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada024`](#insn-00ada024) → [`00ada030`](#insn-00ada030) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada044`](#insn-00ada044) → [`00ada05c`](#insn-00ada05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada050`](#insn-00ada050) → [`00ada068`](#insn-00ada068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada058`](#insn-00ada058) → [`00ada060`](#insn-00ada060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada064`](#insn-00ada064) → [`00ada080`](#insn-00ada080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada084`](#insn-00ada084) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada088`](#insn-00ada088) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada08c`](#insn-00ada08c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad9efc`](#insn-00ad9efc)

~~~json
{
  "source": "00ad9efc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f00`](#insn-00ad9f00)

~~~json
{
  "source": "00ad9f00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f04`](#insn-00ad9f04)

~~~json
{
  "source": "00ad9f04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f24`](#insn-00ad9f24)

~~~json
{
  "source": "00ad9f24",
  "target": "00ad9f34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f28`](#insn-00ad9f28)

~~~json
{
  "source": "00ad9f28",
  "target": "00ad9f48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f30`](#insn-00ad9f30)

~~~json
{
  "source": "00ad9f30",
  "target": "00ad9f3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f50`](#insn-00ad9f50)

~~~json
{
  "source": "00ad9f50",
  "target": "00ad9f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f58`](#insn-00ad9f58)

~~~json
{
  "source": "00ad9f58",
  "target": "00ad9f70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f60`](#insn-00ad9f60)

~~~json
{
  "source": "00ad9f60",
  "target": "00ad9f68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f6c`](#insn-00ad9f6c)

~~~json
{
  "source": "00ad9f6c",
  "target": "00ad9f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9f9c`](#insn-00ad9f9c)

~~~json
{
  "source": "00ad9f9c",
  "target": "00ad9fac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9fa0`](#insn-00ad9fa0)

~~~json
{
  "source": "00ad9fa0",
  "target": "00ad9fc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9fa8`](#insn-00ad9fa8)

~~~json
{
  "source": "00ad9fa8",
  "target": "00ad9fb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9fc8`](#insn-00ad9fc8)

~~~json
{
  "source": "00ad9fc8",
  "target": "00ad9fe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9fd4`](#insn-00ad9fd4)

~~~json
{
  "source": "00ad9fd4",
  "target": "00ad9fec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9fdc`](#insn-00ad9fdc)

~~~json
{
  "source": "00ad9fdc",
  "target": "00ad9fe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad9fe8`](#insn-00ad9fe8)

~~~json
{
  "source": "00ad9fe8",
  "target": "00ada004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada018`](#insn-00ada018)

~~~json
{
  "source": "00ada018",
  "target": "00ada028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada01c`](#insn-00ada01c)

~~~json
{
  "source": "00ada01c",
  "target": "00ada03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada024`](#insn-00ada024)

~~~json
{
  "source": "00ada024",
  "target": "00ada030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada044`](#insn-00ada044)

~~~json
{
  "source": "00ada044",
  "target": "00ada05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada050`](#insn-00ada050)

~~~json
{
  "source": "00ada050",
  "target": "00ada068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada058`](#insn-00ada058)

~~~json
{
  "source": "00ada058",
  "target": "00ada060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada064`](#insn-00ada064)

~~~json
{
  "source": "00ada064",
  "target": "00ada080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada084`](#insn-00ada084)

~~~json
{
  "source": "00ada084",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada088`](#insn-00ada088)

~~~json
{
  "source": "00ada088",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada08c`](#insn-00ada08c)

~~~json
{
  "source": "00ada08c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
