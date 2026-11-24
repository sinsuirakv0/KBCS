# 00bddc4c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd824`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd824.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-35cacdd2bd9c57d2a468a19acf537870)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddce8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-c307cbe4bd1f7d2a3f3cc0fe4bf6942d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddc4c",
  "name": "_ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "187c95eda898727c73438e4ce644ea86714a327cb7260b298c16f8bd4ba4714d",
  "source_text_sha256": "187c95eda898727c73438e4ce644ea86714a327cb7260b298c16f8bd4ba4714d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddc4c",
        "00bddcb7"
      ]
    ],
    "bytes_sha256": "4a5a1e97f745abcad0287b37a2d5d7fe8947ea9d5f5c7b0e268dfc66e2b45af1",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 494 bytes

~~~c

bool _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126e30 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126e28,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126e30 = iVar2 == 0;
    bVar1 = (bool)DAT_01126e30;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddc4c"></a> `00bddc4c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddc50"></a> `00bddc50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddc54"></a> `00bddc54` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddc58"></a> `00bddc58` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddc5c"></a> `00bddc5c` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddc60"></a> `00bddc60` | `a8 c2 78 39` | ldrb w8,[x21, #0xe30] | `FALL_THROUGH`
<a id="insn-00bddc64"></a> `00bddc64` | `68 00 00 34` | cbz w8,0x00bddc70 | `CONDITIONAL_JUMP`
<a id="insn-00bddc68"></a> `00bddc68` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bddc6c"></a> `00bddc6c` | `0f 00 00 14` | b 0x00bddca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bddc70"></a> `00bddc70` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bddc74"></a> `00bddc74` | `49 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddc78"></a> `00bddc78` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bddc7c"></a> `00bddc7c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bddc80"></a> `00bddc80` | `21 15 47 f9` | ldr x1,[x9, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddc84"></a> `00bddc84` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bddc88"></a> `00bddc88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddc8c"></a> `00bddc8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bddc90"></a> `00bddc90` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bddc94"></a> `00bddc94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddc98"></a> `00bddc98` | `b2 f4 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bddc9c"></a> `00bddc9c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bddca0"></a> `00bddca0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bddca4"></a> `00bddca4` | `a0 c2 38 39` | strb w0,[x21, #0xe30] | `FALL_THROUGH`
<a id="insn-00bddca8"></a> `00bddca8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddcac"></a> `00bddcac` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddcb0"></a> `00bddcb0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bddcb4"></a> `00bddcb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddc4c`](#insn-00bddc4c) 範囲 `[['00bddc4c', '00bddc67']]`
  - `CONDITIONAL_JUMP` [`00bddc64`](#insn-00bddc64) → [`00bddc70`](#insn-00bddc70)
  - `FALL_THROUGH` [`00bddc64`](#insn-00bddc64) → [`00bddc68`](#insn-00bddc68)
- ブロック [`00bddc68`](#insn-00bddc68) 範囲 `[['00bddc68', '00bddc6f']]`
  - `UNCONDITIONAL_JUMP` [`00bddc6c`](#insn-00bddc6c) → [`00bddca8`](#insn-00bddca8)
- ブロック [`00bddc70`](#insn-00bddc70) 範囲 `[['00bddc70', '00bddca7']]`
  - `FALL_THROUGH` [`00bddca4`](#insn-00bddca4) → [`00bddca8`](#insn-00bddca8)
- ブロック [`00bddca8`](#insn-00bddca8) 範囲 `[['00bddca8', '00bddcb7']]`

## 命令位置別の参照

- [`00bddc4c`](#insn-00bddc4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc50`](#insn-00bddc50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc54`](#insn-00bddc54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc60`](#insn-00bddc60) → `01126e30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddc64`](#insn-00bddc64) → [`00bddc70`](#insn-00bddc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc6c`](#insn-00bddc6c) → [`00bddca8`](#insn-00bddca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc80`](#insn-00bddc80) → `01126e28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddc98`](#insn-00bddc98) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bddca4`](#insn-00bddca4) → `01126e30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddca8`](#insn-00bddca8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcac`](#insn-00bddcac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddc4c`](#insn-00bddc4c)

~~~json
{
  "source": "00bddc4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc50`](#insn-00bddc50)

~~~json
{
  "source": "00bddc50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc54`](#insn-00bddc54)

~~~json
{
  "source": "00bddc54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc60`](#insn-00bddc60)

~~~json
{
  "source": "00bddc60",
  "target": "01126e30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddc64`](#insn-00bddc64)

~~~json
{
  "source": "00bddc64",
  "target": "00bddc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc6c`](#insn-00bddc6c)

~~~json
{
  "source": "00bddc6c",
  "target": "00bddca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc80`](#insn-00bddc80)

~~~json
{
  "source": "00bddc80",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddc98`](#insn-00bddc98)

~~~json
{
  "source": "00bddc98",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddca4`](#insn-00bddca4)

~~~json
{
  "source": "00bddca4",
  "target": "01126e30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddca8`](#insn-00bddca8)

~~~json
{
  "source": "00bddca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcac`](#insn-00bddcac)

~~~json
{
  "source": "00bddcac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
