# 00b0ccac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aad21c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-77ccbddbf649cb2ab06cb99de513a310)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b0d0d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0067.md#compare-431a6519d01286010a842c7b3ee1b2c1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0ccac",
  "name": "FUN_00b0ccac",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee9437754fa8f60bb46b7a1d08f634830168304821feb74a93e14eece91229d2",
  "source_text_sha256": "ee9437754fa8f60bb46b7a1d08f634830168304821feb74a93e14eece91229d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0ccac",
        "00b0cd33"
      ]
    ],
    "bytes_sha256": "3477796a85bc17d74ca2d61492e1bc8fe577abe6f34f97c65e50d93e9430e98e",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008b9134](../008b9/008b9134.md)
- [00b0b218](../00b0b/00b0b218.md)
- [00b0be2c](../00b0b/00b0be2c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 714 bytes

~~~c

void FUN_00b0ccac(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  uint uVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  uVar1 = *param_4;
  if (*param_3 == 5) {
    lVar3 = *(long *)(param_1 + 8);
    if (uVar1 == 1) {
      FUN_00b0b218(lVar3,*(undefined8 *)(param_1 + 0x10),*(undefined8 *)(param_1 + 0x18),
                   *(undefined4 *)(lVar3 + 0x48));
      return;
    }
    if (uVar1 == 0) {
      FUN_00b0be2c(lVar3,*(undefined4 *)(lVar3 + 0x48),0xffffffff,0,0);
      return;
    }
  }
  else if ((*param_3 == 2) && (uVar1 < 2)) {
    uVar4 = *param_2;
    uVar2 = FUN_0047acb4();
    FUN_0047cd94(uVar2,0xb,0);
    FUN_008b9134(uVar4);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0ccac"></a> `00b0ccac` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-00b0ccb0"></a> `00b0ccb0` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-00b0ccb4"></a> `00b0ccb4` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00b0ccb8"></a> `00b0ccb8` | `20 02 00 54` | b.eq 0x00b0ccfc | `CONDITIONAL_JUMP`
<a id="insn-00b0ccbc"></a> `00b0ccbc` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-00b0ccc0"></a> `00b0ccc0` | `21 03 00 54` | b.ne 0x00b0cd24 | `CONDITIONAL_JUMP`
<a id="insn-00b0ccc4"></a> `00b0ccc4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ccc8"></a> `00b0ccc8` | `e8 02 00 54` | b.hi 0x00b0cd24 | `CONDITIONAL_JUMP`
<a id="insn-00b0cccc"></a> `00b0cccc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b0ccd0"></a> `00b0ccd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ccd4"></a> `00b0ccd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b0ccd8"></a> `00b0ccd8` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00b0ccdc"></a> `00b0ccdc` | `f6 b7 e5 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cce0"></a> `00b0cce0` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00b0cce4"></a> `00b0cce4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b0cce8"></a> `00b0cce8` | `2b c0 e5 97` | bl 0x0047cd94 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ccec"></a> `00b0ccec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0ccf0"></a> `00b0ccf0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ccf4"></a> `00b0ccf4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b0ccf8"></a> `00b0ccf8` | `0f b1 f6 17` | b 0x008b9134 | `CALL_TERMINATOR`
<a id="insn-00b0ccfc"></a> `00b0ccfc` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00b0cd00"></a> `00b0cd00` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cd04"></a> `00b0cd04` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cd08"></a> `00b0cd08` | `00 01 00 54` | b.eq 0x00b0cd28 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd0c"></a> `00b0cd0c` | `c8 00 00 35` | cbnz w8,0x00b0cd24 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd10"></a> `00b0cd10` | `01 48 40 b9` | ldr w1,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00b0cd14"></a> `00b0cd14` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00b0cd18"></a> `00b0cd18` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00b0cd1c"></a> `00b0cd1c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b0cd20"></a> `00b0cd20` | `43 fc ff 17` | b 0x00b0be2c | `CALL_TERMINATOR`
<a id="insn-00b0cd24"></a> `00b0cd24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0cd28"></a> `00b0cd28` | `21 09 41 a9` | ldp x1,x2,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cd2c"></a> `00b0cd2c` | `03 48 40 b9` | ldr w3,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00b0cd30"></a> `00b0cd30` | `3a f9 ff 17` | b 0x00b0b218 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0ccac`](#insn-00b0ccac) 範囲 `[['00b0ccac', '00b0ccbb']]`
  - `CONDITIONAL_JUMP` [`00b0ccb8`](#insn-00b0ccb8) → [`00b0ccfc`](#insn-00b0ccfc)
  - `FALL_THROUGH` [`00b0ccb8`](#insn-00b0ccb8) → [`00b0ccbc`](#insn-00b0ccbc)
- ブロック [`00b0ccbc`](#insn-00b0ccbc) 範囲 `[['00b0ccbc', '00b0ccc3']]`
  - `CONDITIONAL_JUMP` [`00b0ccc0`](#insn-00b0ccc0) → [`00b0cd24`](#insn-00b0cd24)
  - `FALL_THROUGH` [`00b0ccc0`](#insn-00b0ccc0) → [`00b0ccc4`](#insn-00b0ccc4)
- ブロック [`00b0ccc4`](#insn-00b0ccc4) 範囲 `[['00b0ccc4', '00b0cccb']]`
  - `CONDITIONAL_JUMP` [`00b0ccc8`](#insn-00b0ccc8) → [`00b0cd24`](#insn-00b0cd24)
  - `FALL_THROUGH` [`00b0ccc8`](#insn-00b0ccc8) → [`00b0cccc`](#insn-00b0cccc)
- ブロック [`00b0cccc`](#insn-00b0cccc) 範囲 `[['00b0cccc', '00b0ccfb']]`
- ブロック [`00b0ccfc`](#insn-00b0ccfc) 範囲 `[['00b0ccfc', '00b0cd0b']]`
  - `CONDITIONAL_JUMP` [`00b0cd08`](#insn-00b0cd08) → [`00b0cd28`](#insn-00b0cd28)
  - `FALL_THROUGH` [`00b0cd08`](#insn-00b0cd08) → [`00b0cd0c`](#insn-00b0cd0c)
- ブロック [`00b0cd0c`](#insn-00b0cd0c) 範囲 `[['00b0cd0c', '00b0cd0f']]`
  - `CONDITIONAL_JUMP` [`00b0cd0c`](#insn-00b0cd0c) → [`00b0cd24`](#insn-00b0cd24)
  - `FALL_THROUGH` [`00b0cd0c`](#insn-00b0cd0c) → [`00b0cd10`](#insn-00b0cd10)
- ブロック [`00b0cd10`](#insn-00b0cd10) 範囲 `[['00b0cd10', '00b0cd23']]`
- ブロック [`00b0cd24`](#insn-00b0cd24) 範囲 `[['00b0cd24', '00b0cd27']]`
- ブロック [`00b0cd28`](#insn-00b0cd28) 範囲 `[['00b0cd28', '00b0cd33']]`

## 命令位置別の参照

- [`00b0ccb8`](#insn-00b0ccb8) → [`00b0ccfc`](#insn-00b0ccfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccc0`](#insn-00b0ccc0) → [`00b0cd24`](#insn-00b0cd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccc8`](#insn-00b0ccc8) → [`00b0cd24`](#insn-00b0cd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cccc`](#insn-00b0cccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccd0`](#insn-00b0ccd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccdc`](#insn-00b0ccdc) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00b0cce8`](#insn-00b0cce8) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccf0`](#insn-00b0ccf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccf4`](#insn-00b0ccf4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccf8`](#insn-00b0ccf8) → [`008b9134`](../008b9/008b9134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9134` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd08`](#insn-00b0cd08) → [`00b0cd28`](#insn-00b0cd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd0c`](#insn-00b0cd0c) → [`00b0cd24`](#insn-00b0cd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd20`](#insn-00b0cd20) → [`00b0be2c`](../00b0b/00b0be2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0be2c` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd30`](#insn-00b0cd30) → [`00b0b218`](../00b0b/00b0b218.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0b218` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0ccb8`](#insn-00b0ccb8)

~~~json
{
  "source": "00b0ccb8",
  "target": "00b0ccfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccc0`](#insn-00b0ccc0)

~~~json
{
  "source": "00b0ccc0",
  "target": "00b0cd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccc8`](#insn-00b0ccc8)

~~~json
{
  "source": "00b0ccc8",
  "target": "00b0cd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cccc`](#insn-00b0cccc)

~~~json
{
  "source": "00b0cccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccd0`](#insn-00b0ccd0)

~~~json
{
  "source": "00b0ccd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccdc`](#insn-00b0ccdc)

~~~json
{
  "source": "00b0ccdc",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cce8`](#insn-00b0cce8)

~~~json
{
  "source": "00b0cce8",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ccf0`](#insn-00b0ccf0)

~~~json
{
  "source": "00b0ccf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccf4`](#insn-00b0ccf4)

~~~json
{
  "source": "00b0ccf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccf8`](#insn-00b0ccf8)

~~~json
{
  "source": "00b0ccf8",
  "target": "008b9134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cd08`](#insn-00b0cd08)

~~~json
{
  "source": "00b0cd08",
  "target": "00b0cd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd0c`](#insn-00b0cd0c)

~~~json
{
  "source": "00b0cd0c",
  "target": "00b0cd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd20`](#insn-00b0cd20)

~~~json
{
  "source": "00b0cd20",
  "target": "00b0be2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cd30`](#insn-00b0cd30)

~~~json
{
  "source": "00b0cd30",
  "target": "00b0b218",
  "target_space": "ram",
  "resolution": "function"
}
~~~
