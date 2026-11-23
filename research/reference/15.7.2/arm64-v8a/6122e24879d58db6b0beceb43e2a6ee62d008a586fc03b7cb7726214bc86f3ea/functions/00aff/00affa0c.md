# 00affa0c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00affad4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-81308fddcb1696b40a330a381c6b0dd4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affa0c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "471c76ad571c7eca2f5f3d9e0c6d435583d40bc33e83968a30a08cd1c6b809be",
  "source_text_sha256": "471c76ad571c7eca2f5f3d9e0c6d435583d40bc33e83968a30a08cd1c6b809be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affa0c",
        "00affab3"
      ]
    ],
    "bytes_sha256": "9fcbbece03e49b06d84f198482bce51cd82c298d27c45ed17bff5bbef5eb457b",
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

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1496 bytes

~~~c

undefined4
_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  undefined4 uVar4;
  long *plVar5;
  long lVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af6358 with catch @ 00affa0c */
                    /* catch() { ... } // from try @ 00af6284 with catch @ 00affa10 */
  lVar1 = param_1 + 8;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af6188 with catch @ 00affa38 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar5 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar5;
  plVar2 = plVar5;
  if (plVar3 == (long *)0x0) {
LAB_00affa74:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
    if ((plVar2 == plVar5) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affa74;
    lVar6 = plVar2[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    if (lVar6 != 0) {
                    /* catch() { ... } // from try @ 00af612c with catch @ 00affaac */
      uVar4 = *(undefined4 *)(lVar6 + 4);
      goto LAB_00affa80;
    }
  }
  uVar4 = 0xffffffff;
LAB_00affa80:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af617c with catch @ 00affa8c */
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affa0c"></a> `00affa0c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affa10"></a> `00affa10` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affa14"></a> `00affa14` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affa18"></a> `00affa18` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affa1c"></a> `00affa1c` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affa20"></a> `00affa20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affa24"></a> `00affa24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa28"></a> `00affa28` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affa2c"></a> `00affa2c` | `3d 78 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00affa30"></a> `00affa30` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affa34"></a> `00affa34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa38"></a> `00affa38` | `3a 78 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00affa3c"></a> `00affa3c` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affa40"></a> `00affa40` | `a9 01 00 b4` | cbz x9,0x00affa74 | `CONDITIONAL_JUMP`
<a id="insn-00affa44"></a> `00affa44` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affa48"></a> `00affa48` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affa4c"></a> `00affa4c` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affa50"></a> `00affa50` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affa54"></a> `00affa54` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affa58"></a> `00affa58` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affa5c"></a> `00affa5c` | `69 ff ff b5` | cbnz x9,0x00affa48 | `CONDITIONAL_JUMP`
<a id="insn-00affa60"></a> `00affa60` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affa64"></a> `00affa64` | `80 00 00 54` | b.eq 0x00affa74 | `CONDITIONAL_JUMP`
<a id="insn-00affa68"></a> `00affa68` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affa6c"></a> `00affa6c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affa70"></a> `00affa70` | `69 01 00 54` | b.ls 0x00affa9c | `CONDITIONAL_JUMP`
<a id="insn-00affa74"></a> `00affa74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa78"></a> `00affa78` | `2e 78 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affa7c"></a> `00affa7c` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00affa80"></a> `00affa80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affa84"></a> `00affa84` | `2b 78 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affa88"></a> `00affa88` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00affa8c"></a> `00affa8c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affa90"></a> `00affa90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affa94"></a> `00affa94` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affa98"></a> `00affa98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affa9c"></a> `00affa9c` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affaa0"></a> `00affaa0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affaa4"></a> `00affaa4` | `23 78 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affaa8"></a> `00affaa8` | `b4 fe ff b4` | cbz x20,0x00affa7c | `CONDITIONAL_JUMP`
<a id="insn-00affaac"></a> `00affaac` | `94 06 40 b9` | ldr w20,[x20, #0x4] | `FALL_THROUGH`
<a id="insn-00affab0"></a> `00affab0` | `f4 ff ff 17` | b 0x00affa80 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affa0c`](#insn-00affa0c) 範囲 `[['00affa0c', '00affa0f']]`
  - `FALL_THROUGH` [`00affa0c`](#insn-00affa0c) → [`00affa10`](#insn-00affa10)
- ブロック [`00affa10`](#insn-00affa10) 範囲 `[['00affa10', '00affa37']]`
  - `FALL_THROUGH` [`00affa34`](#insn-00affa34) → [`00affa38`](#insn-00affa38)
- ブロック [`00affa38`](#insn-00affa38) 範囲 `[['00affa38', '00affa43']]`
  - `CONDITIONAL_JUMP` [`00affa40`](#insn-00affa40) → [`00affa74`](#insn-00affa74)
  - `FALL_THROUGH` [`00affa40`](#insn-00affa40) → [`00affa44`](#insn-00affa44)
- ブロック [`00affa44`](#insn-00affa44) 範囲 `[['00affa44', '00affa47']]`
  - `FALL_THROUGH` [`00affa44`](#insn-00affa44) → [`00affa48`](#insn-00affa48)
- ブロック [`00affa48`](#insn-00affa48) 範囲 `[['00affa48', '00affa5f']]`
  - `CONDITIONAL_JUMP` [`00affa5c`](#insn-00affa5c) → [`00affa48`](#insn-00affa48)
  - `FALL_THROUGH` [`00affa5c`](#insn-00affa5c) → [`00affa60`](#insn-00affa60)
- ブロック [`00affa60`](#insn-00affa60) 範囲 `[['00affa60', '00affa67']]`
  - `CONDITIONAL_JUMP` [`00affa64`](#insn-00affa64) → [`00affa74`](#insn-00affa74)
  - `FALL_THROUGH` [`00affa64`](#insn-00affa64) → [`00affa68`](#insn-00affa68)
- ブロック [`00affa68`](#insn-00affa68) 範囲 `[['00affa68', '00affa73']]`
  - `CONDITIONAL_JUMP` [`00affa70`](#insn-00affa70) → [`00affa9c`](#insn-00affa9c)
  - `FALL_THROUGH` [`00affa70`](#insn-00affa70) → [`00affa74`](#insn-00affa74)
- ブロック [`00affa74`](#insn-00affa74) 範囲 `[['00affa74', '00affa7b']]`
  - `FALL_THROUGH` [`00affa78`](#insn-00affa78) → [`00affa7c`](#insn-00affa7c)
- ブロック [`00affa7c`](#insn-00affa7c) 範囲 `[['00affa7c', '00affa7f']]`
  - `FALL_THROUGH` [`00affa7c`](#insn-00affa7c) → [`00affa80`](#insn-00affa80)
- ブロック [`00affa80`](#insn-00affa80) 範囲 `[['00affa80', '00affa8b']]`
  - `FALL_THROUGH` [`00affa88`](#insn-00affa88) → [`00affa8c`](#insn-00affa8c)
- ブロック [`00affa8c`](#insn-00affa8c) 範囲 `[['00affa8c', '00affa9b']]`
- ブロック [`00affa9c`](#insn-00affa9c) 範囲 `[['00affa9c', '00affaab']]`
  - `CONDITIONAL_JUMP` [`00affaa8`](#insn-00affaa8) → [`00affa7c`](#insn-00affa7c)
  - `FALL_THROUGH` [`00affaa8`](#insn-00affaa8) → [`00affaac`](#insn-00affaac)
- ブロック [`00affaac`](#insn-00affaac) 範囲 `[['00affaac', '00affab3']]`
  - `UNCONDITIONAL_JUMP` [`00affab0`](#insn-00affab0) → [`00affa80`](#insn-00affa80)

## 命令位置別の参照

- [`00affa0c`](#insn-00affa0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa10`](#insn-00affa10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa14`](#insn-00affa14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa2c`](#insn-00affa2c) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00affa38`](#insn-00affa38) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00affa40`](#insn-00affa40) → [`00affa74`](#insn-00affa74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa5c`](#insn-00affa5c) → [`00affa48`](#insn-00affa48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa64`](#insn-00affa64) → [`00affa74`](#insn-00affa74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa70`](#insn-00affa70) → [`00affa9c`](#insn-00affa9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa78`](#insn-00affa78) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affa84`](#insn-00affa84) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affa8c`](#insn-00affa8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affa90`](#insn-00affa90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affaa4`](#insn-00affaa4) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affaa8`](#insn-00affaa8) → [`00affa7c`](#insn-00affa7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affab0`](#insn-00affab0) → [`00affa80`](#insn-00affa80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affa0c`](#insn-00affa0c)

~~~json
{
  "source": "00affa0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa10`](#insn-00affa10)

~~~json
{
  "source": "00affa10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa14`](#insn-00affa14)

~~~json
{
  "source": "00affa14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa2c`](#insn-00affa2c)

~~~json
{
  "source": "00affa2c",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa38`](#insn-00affa38)

~~~json
{
  "source": "00affa38",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa40`](#insn-00affa40)

~~~json
{
  "source": "00affa40",
  "target": "00affa74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa5c`](#insn-00affa5c)

~~~json
{
  "source": "00affa5c",
  "target": "00affa48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa64`](#insn-00affa64)

~~~json
{
  "source": "00affa64",
  "target": "00affa74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa70`](#insn-00affa70)

~~~json
{
  "source": "00affa70",
  "target": "00affa9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa78`](#insn-00affa78)

~~~json
{
  "source": "00affa78",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa84`](#insn-00affa84)

~~~json
{
  "source": "00affa84",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affa8c`](#insn-00affa8c)

~~~json
{
  "source": "00affa8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affa90`](#insn-00affa90)

~~~json
{
  "source": "00affa90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affaa4`](#insn-00affaa4)

~~~json
{
  "source": "00affaa4",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affaa8`](#insn-00affaa8)

~~~json
{
  "source": "00affaa8",
  "target": "00affa7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affab0`](#insn-00affab0)

~~~json
{
  "source": "00affab0",
  "target": "00affa80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
