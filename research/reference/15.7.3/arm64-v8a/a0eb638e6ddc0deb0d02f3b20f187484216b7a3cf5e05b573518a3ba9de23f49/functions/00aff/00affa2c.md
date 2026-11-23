# 00affa2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aff964`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff964.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-9ea416cf9bf1033af1085c2f9481c5ca)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00affa70`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affa70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-f98ea39233a7541d1100f839b37324d7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affa2c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d53e6a9e91a065ed42626fbb2bd1b28fadbf90b30728853e89b42ab3d0ef65e",
  "source_text_sha256": "9d53e6a9e91a065ed42626fbb2bd1b28fadbf90b30728853e89b42ab3d0ef65e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affa2c",
        "00affad3"
      ]
    ],
    "bytes_sha256": "bd6a9d1811dd2803060a8e2816976f0fd353ee67eeb59d106dd120d659e619b6",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1596 bytes

~~~c

undefined4
_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  undefined4 uVar4;
  long *plVar5;
  undefined4 *puVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af6188 with catch @ 00affa38 */
  lVar1 = param_1 + 8;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar5 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar5;
  plVar2 = plVar5;
  if (plVar3 == (long *)0x0) {
LAB_00affa94:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af617c with catch @ 00affa8c */
    if ((plVar2 == plVar5) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affa94;
                    /* catch() { ... } // from try @ 00af60a4 with catch @ 00affabc */
    puVar6 = (undefined4 *)plVar2[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af6094 with catch @ 00affac8 */
    if (puVar6 != (undefined4 *)0x0) {
      uVar4 = *puVar6;
                    /* catch() { ... } // from try @ 00af6078 with catch @ 00affad0 */
      goto LAB_00affaa0;
    }
  }
  uVar4 = 2;
LAB_00affaa0:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af612c with catch @ 00affaac */
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affa2c"></a> `00affa2c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affa30"></a> `00affa30` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affa34"></a> `00affa34` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affa38"></a> `00affa38` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affa3c"></a> `00affa3c` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affa40"></a> `00affa40` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affa44"></a> `00affa44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa48"></a> `00affa48` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affa4c"></a> `00affa4c` | `61 78 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affa50"></a> `00affa50` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affa54"></a> `00affa54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa58"></a> `00affa58` | `5e 78 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affa5c"></a> `00affa5c` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affa60"></a> `00affa60` | `a9 01 00 b4` | cbz x9,0x00affa94 | `CONDITIONAL_JUMP`
<a id="insn-00affa64"></a> `00affa64` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affa68"></a> `00affa68` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affa6c"></a> `00affa6c` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affa70"></a> `00affa70` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affa74"></a> `00affa74` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affa78"></a> `00affa78` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affa7c"></a> `00affa7c` | `69 ff ff b5` | cbnz x9,0x00affa68 | `CONDITIONAL_JUMP`
<a id="insn-00affa80"></a> `00affa80` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affa84"></a> `00affa84` | `80 00 00 54` | b.eq 0x00affa94 | `CONDITIONAL_JUMP`
<a id="insn-00affa88"></a> `00affa88` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affa8c"></a> `00affa8c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affa90"></a> `00affa90` | `69 01 00 54` | b.ls 0x00affabc | `CONDITIONAL_JUMP`
<a id="insn-00affa94"></a> `00affa94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa98"></a> `00affa98` | `52 78 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affa9c"></a> `00affa9c` | `54 00 80 52` | mov w20,#0x2 | `FALL_THROUGH`
<a id="insn-00affaa0"></a> `00affaa0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affaa4"></a> `00affaa4` | `4f 78 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affaa8"></a> `00affaa8` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00affaac"></a> `00affaac` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affab0"></a> `00affab0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affab4"></a> `00affab4` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affab8"></a> `00affab8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affabc"></a> `00affabc` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affac0"></a> `00affac0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affac4"></a> `00affac4` | `47 78 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affac8"></a> `00affac8` | `b4 fe ff b4` | cbz x20,0x00affa9c | `CONDITIONAL_JUMP`
<a id="insn-00affacc"></a> `00affacc` | `94 02 40 b9` | ldr w20,[x20] | `FALL_THROUGH`
<a id="insn-00affad0"></a> `00affad0` | `f4 ff ff 17` | b 0x00affaa0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affa2c`](#insn-00affa2c) 範囲 `[['00affa2c', '00affa37']]`
  - `FALL_THROUGH` [`00affa34`](#insn-00affa34) → [`00affa38`](#insn-00affa38)
- ブロック [`00affa38`](#insn-00affa38) 範囲 `[['00affa38', '00affa63']]`
  - `CONDITIONAL_JUMP` [`00affa60`](#insn-00affa60) → [`00affa94`](#insn-00affa94)
  - `FALL_THROUGH` [`00affa60`](#insn-00affa60) → [`00affa64`](#insn-00affa64)
- ブロック [`00affa64`](#insn-00affa64) 範囲 `[['00affa64', '00affa67']]`
  - `FALL_THROUGH` [`00affa64`](#insn-00affa64) → [`00affa68`](#insn-00affa68)
- ブロック [`00affa68`](#insn-00affa68) 範囲 `[['00affa68', '00affa7f']]`
  - `CONDITIONAL_JUMP` [`00affa7c`](#insn-00affa7c) → [`00affa68`](#insn-00affa68)
  - `FALL_THROUGH` [`00affa7c`](#insn-00affa7c) → [`00affa80`](#insn-00affa80)
- ブロック [`00affa80`](#insn-00affa80) 範囲 `[['00affa80', '00affa87']]`
  - `CONDITIONAL_JUMP` [`00affa84`](#insn-00affa84) → [`00affa94`](#insn-00affa94)
  - `FALL_THROUGH` [`00affa84`](#insn-00affa84) → [`00affa88`](#insn-00affa88)
- ブロック [`00affa88`](#insn-00affa88) 範囲 `[['00affa88', '00affa8b']]`
  - `FALL_THROUGH` [`00affa88`](#insn-00affa88) → [`00affa8c`](#insn-00affa8c)
- ブロック [`00affa8c`](#insn-00affa8c) 範囲 `[['00affa8c', '00affa93']]`
  - `CONDITIONAL_JUMP` [`00affa90`](#insn-00affa90) → [`00affabc`](#insn-00affabc)
  - `FALL_THROUGH` [`00affa90`](#insn-00affa90) → [`00affa94`](#insn-00affa94)
- ブロック [`00affa94`](#insn-00affa94) 範囲 `[['00affa94', '00affa9b']]`
  - `FALL_THROUGH` [`00affa98`](#insn-00affa98) → [`00affa9c`](#insn-00affa9c)
- ブロック [`00affa9c`](#insn-00affa9c) 範囲 `[['00affa9c', '00affa9f']]`
  - `FALL_THROUGH` [`00affa9c`](#insn-00affa9c) → [`00affaa0`](#insn-00affaa0)
- ブロック [`00affaa0`](#insn-00affaa0) 範囲 `[['00affaa0', '00affaab']]`
  - `FALL_THROUGH` [`00affaa8`](#insn-00affaa8) → [`00affaac`](#insn-00affaac)
- ブロック [`00affaac`](#insn-00affaac) 範囲 `[['00affaac', '00affabb']]`
- ブロック [`00affabc`](#insn-00affabc) 範囲 `[['00affabc', '00affac7']]`
  - `FALL_THROUGH` [`00affac4`](#insn-00affac4) → [`00affac8`](#insn-00affac8)
- ブロック [`00affac8`](#insn-00affac8) 範囲 `[['00affac8', '00affacb']]`
  - `CONDITIONAL_JUMP` [`00affac8`](#insn-00affac8) → [`00affa9c`](#insn-00affa9c)
  - `FALL_THROUGH` [`00affac8`](#insn-00affac8) → [`00affacc`](#insn-00affacc)
- ブロック [`00affacc`](#insn-00affacc) 範囲 `[['00affacc', '00affacf']]`
  - `FALL_THROUGH` [`00affacc`](#insn-00affacc) → [`00affad0`](#insn-00affad0)
- ブロック [`00affad0`](#insn-00affad0) 範囲 `[['00affad0', '00affad3']]`
  - `UNCONDITIONAL_JUMP` [`00affad0`](#insn-00affad0) → [`00affaa0`](#insn-00affaa0)

## 命令位置別の参照

- [`00affa2c`](#insn-00affa2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa30`](#insn-00affa30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa34`](#insn-00affa34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa4c`](#insn-00affa4c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affa58`](#insn-00affa58) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affa60`](#insn-00affa60) → [`00affa94`](#insn-00affa94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa7c`](#insn-00affa7c) → [`00affa68`](#insn-00affa68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa84`](#insn-00affa84) → [`00affa94`](#insn-00affa94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa90`](#insn-00affa90) → [`00affabc`](#insn-00affabc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa98`](#insn-00affa98) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affaa4`](#insn-00affaa4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affaac`](#insn-00affaac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affab0`](#insn-00affab0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affac4`](#insn-00affac4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affac8`](#insn-00affac8) → [`00affa9c`](#insn-00affa9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affad0`](#insn-00affad0) → [`00affaa0`](#insn-00affaa0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affa2c`](#insn-00affa2c)

~~~json
{
  "source": "00affa2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa30`](#insn-00affa30)

~~~json
{
  "source": "00affa30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa34`](#insn-00affa34)

~~~json
{
  "source": "00affa34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa4c`](#insn-00affa4c)

~~~json
{
  "source": "00affa4c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa58`](#insn-00affa58)

~~~json
{
  "source": "00affa58",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa60`](#insn-00affa60)

~~~json
{
  "source": "00affa60",
  "target": "00affa94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa7c`](#insn-00affa7c)

~~~json
{
  "source": "00affa7c",
  "target": "00affa68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa84`](#insn-00affa84)

~~~json
{
  "source": "00affa84",
  "target": "00affa94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa90`](#insn-00affa90)

~~~json
{
  "source": "00affa90",
  "target": "00affabc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa98`](#insn-00affa98)

~~~json
{
  "source": "00affa98",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affaa4`](#insn-00affaa4)

~~~json
{
  "source": "00affaa4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affaac`](#insn-00affaac)

~~~json
{
  "source": "00affaac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affab0`](#insn-00affab0)

~~~json
{
  "source": "00affab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affac4`](#insn-00affac4)

~~~json
{
  "source": "00affac4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affac8`](#insn-00affac8)

~~~json
{
  "source": "00affac8",
  "target": "00affa9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affad0`](#insn-00affad0)

~~~json
{
  "source": "00affad0",
  "target": "00affaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
