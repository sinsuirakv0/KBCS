# 00af5ffc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00af5f34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-30b0ad2259c2decd2673cf43e26404d5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00af6040`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6040.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-edbc7ea5c579c487066cfac800e67eac)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5ffc",
  "name": "_ZN8firebase4util17JavaThreadContext6CancelEv",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed28a2abb718edcf1ff404e8350c186595df512c80a1c87998c1aa8b90929e7f",
  "source_text_sha256": "ed28a2abb718edcf1ff404e8350c186595df512c80a1c87998c1aa8b90929e7f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5ffc",
        "00af6073"
      ]
    ],
    "bytes_sha256": "8ef523a06a48f3af2d634b6e68fea096bffca246e304bba0b85100e7bbc02477",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bde310](../00bde/00bde310.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1224 bytes

~~~c

void _ZN8firebase4util17JavaThreadContext6CancelEv(long param_1)

{
  char cVar1;
  long *plVar2;
  
                    /* try { // try from 00af6000 to 00bf6007 has its CatchHandler @ 00affb00 */
  plVar2 = (long *)_ZNK8firebase8internal16JObjectReference9GetJNIEnvEv();
  if (*(long *)(param_1 + 8) != 0) {
    FUN_00551e14(plVar2,*(long *)(param_1 + 8),DAT_010a0390);
                    /* try { // try from 00af6028 to 00bf602f has its CatchHandler @ 00affaf8 */
    cVar1 = (**(code **)(*plVar2 + 0x720))(plVar2);
                    /* try { // try from 00af6038 to 00bf603f has its CatchHandler @ 00affaf0 */
    if (cVar1 != '\0') {
                    /* try { // try from 00af6048 to 00bf604f has its CatchHandler @ 00affae8 */
      (**(code **)(*plVar2 + 0x80))(plVar2);
                    /* try { // try from 00af6058 to 00bf605f has its CatchHandler @ 00affae0 */
                    /* WARNING: Could not recover jumptable at 0x00af6064. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar2 + 0x88))(plVar2);
      return;
    }
  }
                    /* try { // try from 00af6068 to 00bf606f has its CatchHandler @ 00affad8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5ffc"></a> `00af5ffc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af6000"></a> `00af6000` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6004"></a> `00af6004` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af6008"></a> `00af6008` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af600c"></a> `00af600c` | `c1 a0 03 94` | bl 0x00bde310 | `UNCONDITIONAL_CALL`
<a id="insn-00af6010"></a> `00af6010` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af6014"></a> `00af6014` | `a1 02 00 b4` | cbz x1,0x00af6068 | `CONDITIONAL_JUMP`
<a id="insn-00af6018"></a> `00af6018` | `48 2d 00 d0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af601c"></a> `00af601c` | `02 c9 41 f9` | ldr x2,[x8, #0x390] | `FALL_THROUGH`
<a id="insn-00af6020"></a> `00af6020` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af6024"></a> `00af6024` | `7c 6f e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00af6028"></a> `00af6028` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af602c"></a> `00af602c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af6030"></a> `00af6030` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af6034"></a> `00af6034` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af6038"></a> `00af6038` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af603c"></a> `00af603c` | `60 01 00 54` | b.eq 0x00af6068 | `CONDITIONAL_JUMP`
<a id="insn-00af6040"></a> `00af6040` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af6044"></a> `00af6044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af6048"></a> `00af6048` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af604c"></a> `00af604c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af6050"></a> `00af6050` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af6054"></a> `00af6054` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6058"></a> `00af6058` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af605c"></a> `00af605c` | `01 45 40 f9` | ldr x1,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af6060"></a> `00af6060` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af6064"></a> `00af6064` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00af6068"></a> `00af6068` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af606c"></a> `00af606c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af6070"></a> `00af6070` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af5ffc`](#insn-00af5ffc) 範囲 `[['00af5ffc', '00af5fff']]`
  - `FALL_THROUGH` [`00af5ffc`](#insn-00af5ffc) → [`00af6000`](#insn-00af6000)
- ブロック [`00af6000`](#insn-00af6000) 範囲 `[['00af6000', '00af6017']]`
  - `CONDITIONAL_JUMP` [`00af6014`](#insn-00af6014) → [`00af6068`](#insn-00af6068)
  - `FALL_THROUGH` [`00af6014`](#insn-00af6014) → [`00af6018`](#insn-00af6018)
- ブロック [`00af6018`](#insn-00af6018) 範囲 `[['00af6018', '00af6027']]`
  - `FALL_THROUGH` [`00af6024`](#insn-00af6024) → [`00af6028`](#insn-00af6028)
- ブロック [`00af6028`](#insn-00af6028) 範囲 `[['00af6028', '00af6037']]`
  - `FALL_THROUGH` [`00af6034`](#insn-00af6034) → [`00af6038`](#insn-00af6038)
- ブロック [`00af6038`](#insn-00af6038) 範囲 `[['00af6038', '00af603f']]`
  - `CONDITIONAL_JUMP` [`00af603c`](#insn-00af603c) → [`00af6068`](#insn-00af6068)
  - `FALL_THROUGH` [`00af603c`](#insn-00af603c) → [`00af6040`](#insn-00af6040)
- ブロック [`00af6040`](#insn-00af6040) 範囲 `[['00af6040', '00af6047']]`
  - `FALL_THROUGH` [`00af6044`](#insn-00af6044) → [`00af6048`](#insn-00af6048)
- ブロック [`00af6048`](#insn-00af6048) 範囲 `[['00af6048', '00af6057']]`
  - `FALL_THROUGH` [`00af6054`](#insn-00af6054) → [`00af6058`](#insn-00af6058)
- ブロック [`00af6058`](#insn-00af6058) 範囲 `[['00af6058', '00af6067']]`
- ブロック [`00af6068`](#insn-00af6068) 範囲 `[['00af6068', '00af6073']]`

## 命令位置別の参照

- [`00af5ffc`](#insn-00af5ffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6000`](#insn-00af6000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af600c`](#insn-00af600c) → [`00bde310`](../00bde/00bde310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde310` · 推定シンボル `None` · 推定型 `None`
- [`00af6014`](#insn-00af6014) → [`00af6068`](#insn-00af6068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af601c`](#insn-00af601c) → `010a0390`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af6024`](#insn-00af6024) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00af603c`](#insn-00af603c) → [`00af6068`](#insn-00af6068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6054`](#insn-00af6054) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6068`](#insn-00af6068) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5ffc`](#insn-00af5ffc)

~~~json
{
  "source": "00af5ffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6000`](#insn-00af6000)

~~~json
{
  "source": "00af6000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af600c`](#insn-00af600c)

~~~json
{
  "source": "00af600c",
  "target": "00bde310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6014`](#insn-00af6014)

~~~json
{
  "source": "00af6014",
  "target": "00af6068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af601c`](#insn-00af601c)

~~~json
{
  "source": "00af601c",
  "target": "010a0390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0390",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af6024`](#insn-00af6024)

~~~json
{
  "source": "00af6024",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af603c`](#insn-00af603c)

~~~json
{
  "source": "00af603c",
  "target": "00af6068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6054`](#insn-00af6054)

~~~json
{
  "source": "00af6054",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6068`](#insn-00af6068)

~~~json
{
  "source": "00af6068",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
