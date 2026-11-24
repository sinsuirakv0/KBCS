# 006dfbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `006b5e30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md) · 移動量 `+0x29dbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0030.md#compare-61f26865cfca9470da18f18d83b4ed2a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `006dfc2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfc2c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0021.md#compare-6e403c6039574cad2e26cd24704bada0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dfbec",
  "name": "FUN_006dfbec",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84f30f9b495c15e7fbc73cab08e66f93bbac0d39beddf025884adb5d74d8b651",
  "source_text_sha256": "84f30f9b495c15e7fbc73cab08e66f93bbac0d39beddf025884adb5d74d8b651",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dfbec",
        "006dfd87"
      ]
    ],
    "bytes_sha256": "55d840e0029d52d900ea5ef9eedbc0c185eeb980733de38021d9422299440cd5",
    "instruction_count": 103,
    "instruction_bytes": 412,
    "body_bytes": 412,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006ea548](../006ea/006ea548.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00800338](../00800/00800338.md)
- [00805cf4](../00805/00805cf4.md)
- [008514b8](../00851/008514b8.md)
- [0085c10c](../0085c/0085c10c.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2393 bytes

~~~c

void FUN_006dfbec(long param_1)

{
  wchar_t *pwVar1;
  int iVar2;
  undefined4 uVar3;
  long lVar4;
  wchar_t *pwVar5;
  undefined8 uVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  long *plVar9;
  wchar_t *pwVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  
  lVar4 = FUN_008514b8();
  if (*(int *)(lVar4 + 0x44e36c) == -1) {
    pwVar5 = *(wchar_t **)(param_1 + 0x18);
    pwVar1 = *(wchar_t **)(param_1 + 0x20);
    lVar4 = FUN_008514b8();
    pwVar5 = wmemchr(pwVar5,*(wchar_t *)(lVar4 + 0x44e368),(long)pwVar1 - (long)pwVar5 >> 2);
    pwVar10 = *(wchar_t **)(param_1 + 0x20);
    if (pwVar5 != (wchar_t *)0x0) {
      pwVar1 = pwVar5;
    }
    lVar4 = FUN_008514b8();
    if (pwVar1 == pwVar10) {
      uVar3 = FUN_0085c10c(lVar4,1);
    }
    else {
      uVar3 = *(undefined4 *)(lVar4 + 0x44e368);
    }
    lVar4 = FUN_008514b8();
    *(undefined4 *)(lVar4 + 0x44e36c) = uVar3;
  }
  lVar4 = FUN_008514b8();
  iVar2 = *(int *)(lVar4 + 0x44e36c);
                    /* catch() { ... } // from try @ 006dfe78 with catch @ 006dfc9c */
  *(int *)(param_1 + 0x30) = iVar2;
  if (iVar2 != -1) {
    uVar6 = FUN_00800338();
    uVar6 = FUN_00805cf4(uVar6,*(int *)(param_1 + 0x30) % 1000);
    iVar2 = *(int *)(param_1 + 0x30);
    puVar11 = (undefined8 *)(param_1 + 0x58);
    puVar8 = (undefined8 *)*puVar11;
    puVar12 = puVar11;
    if ((undefined8 *)*puVar11 != (undefined8 *)0x0) {
      do {
        while (puVar7 = puVar8, puVar11 = puVar7, iVar2 < *(int *)(puVar7 + 4)) {
          puVar8 = (undefined8 *)*puVar7;
          puVar12 = puVar7;
          if ((undefined8 *)*puVar7 == (undefined8 *)0x0) goto LAB_006dfd1c;
        }
        if (iVar2 <= *(int *)(puVar7 + 4)) goto LAB_006dfd6c;
        puVar8 = (undefined8 *)puVar7[1];
      } while ((undefined8 *)puVar7[1] != (undefined8 *)0x0);
      puVar12 = puVar7 + 1;
    }
LAB_006dfd1c:
    puVar7 = (undefined8 *)_Znwm(0x30);
    *puVar7 = 0;
    puVar7[1] = 0;
    puVar7[2] = puVar11;
    *puVar12 = puVar7;
    plVar9 = *(long **)(param_1 + 0x50);
    *(int *)(puVar7 + 4) = iVar2;
    puVar7[5] = 0;
    puVar8 = puVar7;
    if (*plVar9 != 0) {
      *(long *)(param_1 + 0x50) = *plVar9;
      puVar8 = (undefined8 *)*puVar12;
    }
    FUN_0043bb64(*(undefined8 *)(param_1 + 0x58),puVar8);
    *(long *)(param_1 + 0x60) = *(long *)(param_1 + 0x60) + 1;
LAB_006dfd6c:
    puVar7[5] = uVar6;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006dfbec"></a> `006dfbec` | `e8 0f 1c fc` | str d8,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-006dfbf0"></a> `006dfbf0` | `fd fb 00 a9` | stp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006dfbf4"></a> `006dfbf4` | `f7 0f 00 f9` | str x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006dfbf8"></a> `006dfbf8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dfbfc"></a> `006dfbfc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dfc00"></a> `006dfc00` | `fd 23 00 91` | add x29,sp,#0x8 | `FALL_THROUGH`
<a id="insn-006dfc04"></a> `006dfc04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006dfc08"></a> `006dfc08` | `2c c6 05 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006dfc0c"></a> `006dfc0c` | `88 6d 9c 52` | mov w8,#0xe36c | `FALL_THROUGH`
<a id="insn-006dfc10"></a> `006dfc10` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-006dfc14"></a> `006dfc14` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006dfc18"></a> `006dfc18` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-006dfc1c"></a> `006dfc1c` | `61 03 00 54` | b.ne 0x006dfc88 | `CONDITIONAL_JUMP`
<a id="insn-006dfc20"></a> `006dfc20` | `74 d6 41 a9` | ldp x20,x21,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-006dfc24"></a> `006dfc24` | `25 c6 05 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006dfc28"></a> `006dfc28` | `08 6d 9c 52` | mov w8,#0xe368 | `FALL_THROUGH`
<a id="insn-006dfc2c"></a> `006dfc2c` | `a9 02 14 cb` | sub x9,x21,x20 | `FALL_THROUGH`
<a id="insn-006dfc30"></a> `006dfc30` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-006dfc34"></a> `006dfc34` | `22 fd 42 93` | asr x2,x9,#0x2 | `FALL_THROUGH`
<a id="insn-006dfc38"></a> `006dfc38` | `01 68 68 b8` | ldr w1,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006dfc3c"></a> `006dfc3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006dfc40"></a> `006dfc40` | `04 e1 15 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-006dfc44"></a> `006dfc44` | `74 12 40 f9` | ldr x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006dfc48"></a> `006dfc48` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-006dfc4c"></a> `006dfc4c` | `b5 02 80 9a` | csel x21,x21,x0,eq | `FALL_THROUGH`
<a id="insn-006dfc50"></a> `006dfc50` | `1a c6 05 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006dfc54"></a> `006dfc54` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-006dfc58"></a> `006dfc58` | `a0 00 00 54` | b.eq 0x006dfc6c | `CONDITIONAL_JUMP`
<a id="insn-006dfc5c"></a> `006dfc5c` | `08 6d 9c 52` | mov w8,#0xe368 | `FALL_THROUGH`
<a id="insn-006dfc60"></a> `006dfc60` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-006dfc64"></a> `006dfc64` | `14 68 68 b8` | ldr w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006dfc68"></a> `006dfc68` | `04 00 00 14` | b 0x006dfc78 | `UNCONDITIONAL_JUMP`
<a id="insn-006dfc6c"></a> `006dfc6c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006dfc70"></a> `006dfc70` | `27 f1 05 94` | bl 0x0085c10c | `UNCONDITIONAL_CALL`
<a id="insn-006dfc74"></a> `006dfc74` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-006dfc78"></a> `006dfc78` | `10 c6 05 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006dfc7c"></a> `006dfc7c` | `88 6d 9c 52` | mov w8,#0xe36c | `FALL_THROUGH`
<a id="insn-006dfc80"></a> `006dfc80` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-006dfc84"></a> `006dfc84` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006dfc88"></a> `006dfc88` | `0c c6 05 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006dfc8c"></a> `006dfc8c` | `88 6d 9c 52` | mov w8,#0xe36c | `FALL_THROUGH`
<a id="insn-006dfc90"></a> `006dfc90` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-006dfc94"></a> `006dfc94` | `00 68 68 b8` | ldr w0,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006dfc98"></a> `006dfc98` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-006dfc9c"></a> `006dfc9c` | `60 32 00 b9` | str w0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-006dfca0"></a> `006dfca0` | `80 06 00 54` | b.eq 0x006dfd70 | `CONDITIONAL_JUMP`
<a id="insn-006dfca4"></a> `006dfca4` | `a5 81 04 94` | bl 0x00800338 | `UNCONDITIONAL_CALL`
<a id="insn-006dfca8"></a> `006dfca8` | `68 32 80 b9` | ldrsw x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-006dfcac"></a> `006dfcac` | `69 ba 89 52` | mov w9,#0x4dd3 | `FALL_THROUGH`
<a id="insn-006dfcb0"></a> `006dfcb0` | `49 0c a2 72` | movk w9,#0x1062, LSL #16 | `FALL_THROUGH`
<a id="insn-006dfcb4"></a> `006dfcb4` | `09 7d 29 9b` | smull x9,w8,w9 | `FALL_THROUGH`
<a id="insn-006dfcb8"></a> `006dfcb8` | `2a fd 7f d3` | lsr x10,x9,#0x3f | `FALL_THROUGH`
<a id="insn-006dfcbc"></a> `006dfcbc` | `29 fd 66 93` | asr x9,x9,#0x26 | `FALL_THROUGH`
<a id="insn-006dfcc0"></a> `006dfcc0` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-006dfcc4"></a> `006dfcc4` | `0a 7d 80 52` | mov w10,#0x3e8 | `FALL_THROUGH`
<a id="insn-006dfcc8"></a> `006dfcc8` | `21 a1 0a 1b` | msub w1,w9,w10,w8 | `FALL_THROUGH`
<a id="insn-006dfccc"></a> `006dfccc` | `0a 98 04 94` | bl 0x00805cf4 | `UNCONDITIONAL_CALL`
<a id="insn-006dfcd0"></a> `006dfcd0` | `08 40 60 1e` | fmov d8,d0 | `FALL_THROUGH`
<a id="insn-006dfcd4"></a> `006dfcd4` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-006dfcd8"></a> `006dfcd8` | `75 32 40 b9` | ldr w21,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-006dfcdc"></a> `006dfcdc` | `c8 8e 45 f8` | ldr x8,[x22, #0x58]! | `FALL_THROUGH`
<a id="insn-006dfce0"></a> `006dfce0` | `c8 00 00 b5` | cbnz x8,0x006dfcf8 | `CONDITIONAL_JUMP`
<a id="insn-006dfce4"></a> `006dfce4` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-006dfce8"></a> `006dfce8` | `0d 00 00 14` | b 0x006dfd1c | `UNCONDITIONAL_JUMP`
<a id="insn-006dfcec"></a> `006dfcec` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-006dfcf0"></a> `006dfcf0` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-006dfcf4"></a> `006dfcf4` | `48 01 00 b4` | cbz x8,0x006dfd1c | `CONDITIONAL_JUMP`
<a id="insn-006dfcf8"></a> `006dfcf8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-006dfcfc"></a> `006dfcfc` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-006dfd00"></a> `006dfd00` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-006dfd04"></a> `006dfd04` | `4b ff ff 54` | b.lt 0x006dfcec | `CONDITIONAL_JUMP`
<a id="insn-006dfd08"></a> `006dfd08` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-006dfd0c"></a> `006dfd0c` | `0a 03 00 54` | b.ge 0x006dfd6c | `CONDITIONAL_JUMP`
<a id="insn-006dfd10"></a> `006dfd10` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-006dfd14"></a> `006dfd14` | `28 ff ff b5` | cbnz x8,0x006dfcf8 | `CONDITIONAL_JUMP`
<a id="insn-006dfd18"></a> `006dfd18` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-006dfd1c"></a> `006dfd1c` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-006dfd20"></a> `006dfd20` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-006dfd24"></a> `006dfd24` | `5b df 15 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-006dfd28"></a> `006dfd28` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-006dfd2c"></a> `006dfd2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006dfd30"></a> `006dfd30` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-006dfd34"></a> `006dfd34` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-006dfd38"></a> `006dfd38` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-006dfd3c"></a> `006dfd3c` | `68 2a 40 f9` | ldr x8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-006dfd40"></a> `006dfd40` | `15 20 00 b9` | str w21,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-006dfd44"></a> `006dfd44` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-006dfd48"></a> `006dfd48` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006dfd4c"></a> `006dfd4c` | `68 00 00 b4` | cbz x8,0x006dfd58 | `CONDITIONAL_JUMP`
<a id="insn-006dfd50"></a> `006dfd50` | `68 2a 00 f9` | str x8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-006dfd54"></a> `006dfd54` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-006dfd58"></a> `006dfd58` | `60 2e 40 f9` | ldr x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-006dfd5c"></a> `006dfd5c` | `82 6f f5 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-006dfd60"></a> `006dfd60` | `68 32 40 f9` | ldr x8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-006dfd64"></a> `006dfd64` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006dfd68"></a> `006dfd68` | `68 32 00 f9` | str x8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-006dfd6c"></a> `006dfd6c` | `88 16 00 fd` | str d8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006dfd70"></a> `006dfd70` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dfd74"></a> `006dfd74` | `f7 0f 40 f9` | ldr x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006dfd78"></a> `006dfd78` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dfd7c"></a> `006dfd7c` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006dfd80"></a> `006dfd80` | `e8 07 44 fc` | ldr d8,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-006dfd84"></a> `006dfd84` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dfbec`](#insn-006dfbec) 範囲 `[['006dfbec', '006dfc1f']]`
  - `CONDITIONAL_JUMP` [`006dfc1c`](#insn-006dfc1c) → [`006dfc88`](#insn-006dfc88)
  - `FALL_THROUGH` [`006dfc1c`](#insn-006dfc1c) → [`006dfc20`](#insn-006dfc20)
- ブロック [`006dfc20`](#insn-006dfc20) 範囲 `[['006dfc20', '006dfc5b']]`
  - `CONDITIONAL_JUMP` [`006dfc58`](#insn-006dfc58) → [`006dfc6c`](#insn-006dfc6c)
  - `FALL_THROUGH` [`006dfc58`](#insn-006dfc58) → [`006dfc5c`](#insn-006dfc5c)
- ブロック [`006dfc5c`](#insn-006dfc5c) 範囲 `[['006dfc5c', '006dfc6b']]`
  - `UNCONDITIONAL_JUMP` [`006dfc68`](#insn-006dfc68) → [`006dfc78`](#insn-006dfc78)
- ブロック [`006dfc6c`](#insn-006dfc6c) 範囲 `[['006dfc6c', '006dfc77']]`
  - `FALL_THROUGH` [`006dfc74`](#insn-006dfc74) → [`006dfc78`](#insn-006dfc78)
- ブロック [`006dfc78`](#insn-006dfc78) 範囲 `[['006dfc78', '006dfc87']]`
  - `FALL_THROUGH` [`006dfc84`](#insn-006dfc84) → [`006dfc88`](#insn-006dfc88)
- ブロック [`006dfc88`](#insn-006dfc88) 範囲 `[['006dfc88', '006dfc9b']]`
  - `FALL_THROUGH` [`006dfc98`](#insn-006dfc98) → [`006dfc9c`](#insn-006dfc9c)
- ブロック [`006dfc9c`](#insn-006dfc9c) 範囲 `[['006dfc9c', '006dfca3']]`
  - `CONDITIONAL_JUMP` [`006dfca0`](#insn-006dfca0) → [`006dfd70`](#insn-006dfd70)
  - `FALL_THROUGH` [`006dfca0`](#insn-006dfca0) → [`006dfca4`](#insn-006dfca4)
- ブロック [`006dfca4`](#insn-006dfca4) 範囲 `[['006dfca4', '006dfce3']]`
  - `CONDITIONAL_JUMP` [`006dfce0`](#insn-006dfce0) → [`006dfcf8`](#insn-006dfcf8)
  - `FALL_THROUGH` [`006dfce0`](#insn-006dfce0) → [`006dfce4`](#insn-006dfce4)
- ブロック [`006dfce4`](#insn-006dfce4) 範囲 `[['006dfce4', '006dfceb']]`
  - `UNCONDITIONAL_JUMP` [`006dfce8`](#insn-006dfce8) → [`006dfd1c`](#insn-006dfd1c)
- ブロック [`006dfcec`](#insn-006dfcec) 範囲 `[['006dfcec', '006dfcf7']]`
  - `CONDITIONAL_JUMP` [`006dfcf4`](#insn-006dfcf4) → [`006dfd1c`](#insn-006dfd1c)
  - `FALL_THROUGH` [`006dfcf4`](#insn-006dfcf4) → [`006dfcf8`](#insn-006dfcf8)
- ブロック [`006dfcf8`](#insn-006dfcf8) 範囲 `[['006dfcf8', '006dfd07']]`
  - `CONDITIONAL_JUMP` [`006dfd04`](#insn-006dfd04) → [`006dfcec`](#insn-006dfcec)
  - `FALL_THROUGH` [`006dfd04`](#insn-006dfd04) → [`006dfd08`](#insn-006dfd08)
- ブロック [`006dfd08`](#insn-006dfd08) 範囲 `[['006dfd08', '006dfd0f']]`
  - `CONDITIONAL_JUMP` [`006dfd0c`](#insn-006dfd0c) → [`006dfd6c`](#insn-006dfd6c)
  - `FALL_THROUGH` [`006dfd0c`](#insn-006dfd0c) → [`006dfd10`](#insn-006dfd10)
- ブロック [`006dfd10`](#insn-006dfd10) 範囲 `[['006dfd10', '006dfd17']]`
  - `CONDITIONAL_JUMP` [`006dfd14`](#insn-006dfd14) → [`006dfcf8`](#insn-006dfcf8)
  - `FALL_THROUGH` [`006dfd14`](#insn-006dfd14) → [`006dfd18`](#insn-006dfd18)
- ブロック [`006dfd18`](#insn-006dfd18) 範囲 `[['006dfd18', '006dfd1b']]`
  - `FALL_THROUGH` [`006dfd18`](#insn-006dfd18) → [`006dfd1c`](#insn-006dfd1c)
- ブロック [`006dfd1c`](#insn-006dfd1c) 範囲 `[['006dfd1c', '006dfd4f']]`
  - `CONDITIONAL_JUMP` [`006dfd4c`](#insn-006dfd4c) → [`006dfd58`](#insn-006dfd58)
  - `FALL_THROUGH` [`006dfd4c`](#insn-006dfd4c) → [`006dfd50`](#insn-006dfd50)
- ブロック [`006dfd50`](#insn-006dfd50) 範囲 `[['006dfd50', '006dfd57']]`
  - `FALL_THROUGH` [`006dfd54`](#insn-006dfd54) → [`006dfd58`](#insn-006dfd58)
- ブロック [`006dfd58`](#insn-006dfd58) 範囲 `[['006dfd58', '006dfd6b']]`
  - `FALL_THROUGH` [`006dfd68`](#insn-006dfd68) → [`006dfd6c`](#insn-006dfd6c)
- ブロック [`006dfd6c`](#insn-006dfd6c) 範囲 `[['006dfd6c', '006dfd6f']]`
  - `FALL_THROUGH` [`006dfd6c`](#insn-006dfd6c) → [`006dfd70`](#insn-006dfd70)
- ブロック [`006dfd70`](#insn-006dfd70) 範囲 `[['006dfd70', '006dfd87']]`

## 命令位置別の参照

- [`006dfbec`](#insn-006dfbec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbf0`](#insn-006dfbf0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbf4`](#insn-006dfbf4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbf8`](#insn-006dfbf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbfc`](#insn-006dfbfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfc08`](#insn-006dfc08) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006dfc1c`](#insn-006dfc1c) → [`006dfc88`](#insn-006dfc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfc24`](#insn-006dfc24) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006dfc40`](#insn-006dfc40) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`006dfc50`](#insn-006dfc50) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006dfc58`](#insn-006dfc58) → [`006dfc6c`](#insn-006dfc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfc68`](#insn-006dfc68) → [`006dfc78`](#insn-006dfc78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfc70`](#insn-006dfc70) → [`0085c10c`](../0085c/0085c10c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085c10c` · 推定シンボル `None` · 推定型 `None`
- [`006dfc78`](#insn-006dfc78) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006dfc88`](#insn-006dfc88) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006dfca0`](#insn-006dfca0) → [`006dfd70`](#insn-006dfd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfca4`](#insn-006dfca4) → [`00800338`](../00800/00800338.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800338` · 推定シンボル `None` · 推定型 `None`
- [`006dfccc`](#insn-006dfccc) → [`00805cf4`](../00805/00805cf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00805cf4` · 推定シンボル `None` · 推定型 `None`
- [`006dfce0`](#insn-006dfce0) → [`006dfcf8`](#insn-006dfcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfce8`](#insn-006dfce8) → [`006dfd1c`](#insn-006dfd1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfcf4`](#insn-006dfcf4) → [`006dfd1c`](#insn-006dfd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd04`](#insn-006dfd04) → [`006dfcec`](#insn-006dfcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd0c`](#insn-006dfd0c) → [`006dfd6c`](#insn-006dfd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd14`](#insn-006dfd14) → [`006dfcf8`](#insn-006dfcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd24`](#insn-006dfd24) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`006dfd4c`](#insn-006dfd4c) → [`006dfd58`](#insn-006dfd58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd5c`](#insn-006dfd5c) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`006dfd70`](#insn-006dfd70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd74`](#insn-006dfd74) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd78`](#insn-006dfd78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfd7c`](#insn-006dfd7c) → `Stack[-0x38]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006dfbec`](#insn-006dfbec)

~~~json
{
  "source": "006dfbec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbf0`](#insn-006dfbf0)

~~~json
{
  "source": "006dfbf0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbf4`](#insn-006dfbf4)

~~~json
{
  "source": "006dfbf4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbf8`](#insn-006dfbf8)

~~~json
{
  "source": "006dfbf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbfc`](#insn-006dfbfc)

~~~json
{
  "source": "006dfbfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfc08`](#insn-006dfc08)

~~~json
{
  "source": "006dfc08",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfc1c`](#insn-006dfc1c)

~~~json
{
  "source": "006dfc1c",
  "target": "006dfc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfc24`](#insn-006dfc24)

~~~json
{
  "source": "006dfc24",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfc40`](#insn-006dfc40)

~~~json
{
  "source": "006dfc40",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfc50`](#insn-006dfc50)

~~~json
{
  "source": "006dfc50",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfc58`](#insn-006dfc58)

~~~json
{
  "source": "006dfc58",
  "target": "006dfc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfc68`](#insn-006dfc68)

~~~json
{
  "source": "006dfc68",
  "target": "006dfc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfc70`](#insn-006dfc70)

~~~json
{
  "source": "006dfc70",
  "target": "0085c10c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfc78`](#insn-006dfc78)

~~~json
{
  "source": "006dfc78",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfc88`](#insn-006dfc88)

~~~json
{
  "source": "006dfc88",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfca0`](#insn-006dfca0)

~~~json
{
  "source": "006dfca0",
  "target": "006dfd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfca4`](#insn-006dfca4)

~~~json
{
  "source": "006dfca4",
  "target": "00800338",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfccc`](#insn-006dfccc)

~~~json
{
  "source": "006dfccc",
  "target": "00805cf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfce0`](#insn-006dfce0)

~~~json
{
  "source": "006dfce0",
  "target": "006dfcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfce8`](#insn-006dfce8)

~~~json
{
  "source": "006dfce8",
  "target": "006dfd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfcf4`](#insn-006dfcf4)

~~~json
{
  "source": "006dfcf4",
  "target": "006dfd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd04`](#insn-006dfd04)

~~~json
{
  "source": "006dfd04",
  "target": "006dfcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd0c`](#insn-006dfd0c)

~~~json
{
  "source": "006dfd0c",
  "target": "006dfd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd14`](#insn-006dfd14)

~~~json
{
  "source": "006dfd14",
  "target": "006dfcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd24`](#insn-006dfd24)

~~~json
{
  "source": "006dfd24",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfd4c`](#insn-006dfd4c)

~~~json
{
  "source": "006dfd4c",
  "target": "006dfd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd5c`](#insn-006dfd5c)

~~~json
{
  "source": "006dfd5c",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfd70`](#insn-006dfd70)

~~~json
{
  "source": "006dfd70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd74`](#insn-006dfd74)

~~~json
{
  "source": "006dfd74",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd78`](#insn-006dfd78)

~~~json
{
  "source": "006dfd78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfd7c`](#insn-006dfd7c)

~~~json
{
  "source": "006dfd7c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
