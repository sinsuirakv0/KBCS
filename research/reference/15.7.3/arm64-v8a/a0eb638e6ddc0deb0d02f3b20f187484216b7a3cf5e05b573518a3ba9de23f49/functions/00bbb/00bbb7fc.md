# 00bbb7fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbb734`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb734.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/reference_unresolved-0017.md#compare-57ac1e9a6b0f7e03147bee6fa4d24471)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbb840`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb840.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/reference_unresolved-0016.md#compare-656c049cb2fd87a7df1949a6dcb7149f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb7fc",
  "name": "FUN_00bbb7fc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc14a8f2f55abc751ddd38887e6bb3886273cd3a3da6723d5a9eea4686342132",
  "source_text_sha256": "fc14a8f2f55abc751ddd38887e6bb3886273cd3a3da6723d5a9eea4686342132",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb7fc",
        "00bbb88f"
      ]
    ],
    "bytes_sha256": "c9ddbf86c89035c1d9641c2e976d42d94c04fc114dd1da187f31e51319576d94",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1752 bytes

~~~c

void FUN_00bbb7fc(long param_1,long param_2,long param_3,undefined4 param_4)

{
                    /* catch() { ... } // from try @ 00bbb334 with catch @ 00bbb808 */
                    /* catch() { ... } // from try @ 00bbb254 with catch @ 00bbb80c */
  if (*(long *)(param_1 + 8) != *(long *)(*(long *)(param_2 + 0x10) + 8)) {
                    /* WARNING: Could not recover jumptable at 0x00bbb820. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(**(long **)(param_1 + 0x10) + 0x38))();
    return;
  }
                    /* catch() { ... } // from try @ 00bbb244 with catch @ 00bbb824 */
  if (*(int *)(param_2 + 0x3c) != 0) {
                    /* catch() { ... } // from try @ 00bbb238 with catch @ 00bbb838 */
                    /* catch() { ... } // from try @ 00bbb044 with catch @ 00bbb83c
                       catch() { ... } // from try @ 00bbb124 with catch @ 00bbb83c */
                    /* catch() { ... } // from try @ 00bbafc8 with catch @ 00bbb840 */
    if ((*(long *)(param_2 + 0x28) == *(long *)(param_2 + 0x50)) &&
       (*(long *)(param_2 + 0x20) == param_3)) {
      if (*(int *)(param_2 + 0x30) == 2) {
        *(undefined4 *)(param_2 + 0x30) = param_4;
        return;
      }
    }
    else {
      *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
                    /* catch() { ... } // from try @ 00bbafb8 with catch @ 00bbb858 */
      *(undefined4 *)(param_2 + 0x30) = 2;
      *(undefined1 *)(param_2 + 0x4e) = 1;
    }
    return;
  }
  *(undefined4 *)(param_2 + 0x30) = param_4;
  *(undefined4 *)(param_2 + 0x3c) = 1;
  *(long *)(param_2 + 0x20) = param_3;
  *(undefined8 *)(param_2 + 0x28) = *(undefined8 *)(param_2 + 0x50);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb7fc"></a> `00bbb7fc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbb800"></a> `00bbb800` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb804"></a> `00bbb804` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb808"></a> `00bbb808` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb80c"></a> `00bbb80c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbb810"></a> `00bbb810` | `a0 00 00 54` | b.eq 0x00bbb824 | `CONDITIONAL_JUMP`
<a id="insn-00bbb814"></a> `00bbb814` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb818"></a> `00bbb818` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbb81c"></a> `00bbb81c` | `10 1d 40 f9` | ldr x16,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb820"></a> `00bbb820` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bbb824"></a> `00bbb824` | `28 3c 40 b9` | ldr w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb828"></a> `00bbb828` | `e8 01 00 34` | cbz w8,0x00bbb864 | `CONDITIONAL_JUMP`
<a id="insn-00bbb82c"></a> `00bbb82c` | `29 14 40 f9` | ldr x9,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb830"></a> `00bbb830` | `2a 28 40 f9` | ldr x10,[x1, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb834"></a> `00bbb834` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbb838"></a> `00bbb838` | `81 00 00 54` | b.ne 0x00bbb848 | `CONDITIONAL_JUMP`
<a id="insn-00bbb83c"></a> `00bbb83c` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb840"></a> `00bbb840` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bbb844"></a> `00bbb844` | `c0 01 00 54` | b.eq 0x00bbb87c | `CONDITIONAL_JUMP`
<a id="insn-00bbb848"></a> `00bbb848` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb84c"></a> `00bbb84c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb850"></a> `00bbb850` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb854"></a> `00bbb854` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb858"></a> `00bbb858` | `29 30 00 b9` | str w9,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb85c"></a> `00bbb85c` | `28 38 01 39` | strb w8,[x1, #0x4e] | `FALL_THROUGH`
<a id="insn-00bbb860"></a> `00bbb860` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb864"></a> `00bbb864` | `28 28 40 f9` | ldr x8,[x1, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb868"></a> `00bbb868` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb86c"></a> `00bbb86c` | `23 30 00 b9` | str w3,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb870"></a> `00bbb870` | `29 3c 00 b9` | str w9,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb874"></a> `00bbb874` | `22 20 02 a9` | stp x2,x8,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb878"></a> `00bbb878` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb87c"></a> `00bbb87c` | `28 30 40 b9` | ldr w8,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb880"></a> `00bbb880` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb884"></a> `00bbb884` | `e1 fe ff 54` | b.ne 0x00bbb860 | `CONDITIONAL_JUMP`
<a id="insn-00bbb888"></a> `00bbb888` | `23 30 00 b9` | str w3,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb88c"></a> `00bbb88c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb7fc`](#insn-00bbb7fc) 範囲 `[['00bbb7fc', '00bbb807']]`
  - `FALL_THROUGH` [`00bbb804`](#insn-00bbb804) → [`00bbb808`](#insn-00bbb808)
- ブロック [`00bbb808`](#insn-00bbb808) 範囲 `[['00bbb808', '00bbb80b']]`
  - `FALL_THROUGH` [`00bbb808`](#insn-00bbb808) → [`00bbb80c`](#insn-00bbb80c)
- ブロック [`00bbb80c`](#insn-00bbb80c) 範囲 `[['00bbb80c', '00bbb813']]`
  - `CONDITIONAL_JUMP` [`00bbb810`](#insn-00bbb810) → [`00bbb824`](#insn-00bbb824)
  - `FALL_THROUGH` [`00bbb810`](#insn-00bbb810) → [`00bbb814`](#insn-00bbb814)
- ブロック [`00bbb814`](#insn-00bbb814) 範囲 `[['00bbb814', '00bbb823']]`
- ブロック [`00bbb824`](#insn-00bbb824) 範囲 `[['00bbb824', '00bbb82b']]`
  - `CONDITIONAL_JUMP` [`00bbb828`](#insn-00bbb828) → [`00bbb864`](#insn-00bbb864)
  - `FALL_THROUGH` [`00bbb828`](#insn-00bbb828) → [`00bbb82c`](#insn-00bbb82c)
- ブロック [`00bbb82c`](#insn-00bbb82c) 範囲 `[['00bbb82c', '00bbb837']]`
  - `FALL_THROUGH` [`00bbb834`](#insn-00bbb834) → [`00bbb838`](#insn-00bbb838)
- ブロック [`00bbb838`](#insn-00bbb838) 範囲 `[['00bbb838', '00bbb83b']]`
  - `CONDITIONAL_JUMP` [`00bbb838`](#insn-00bbb838) → [`00bbb848`](#insn-00bbb848)
  - `FALL_THROUGH` [`00bbb838`](#insn-00bbb838) → [`00bbb83c`](#insn-00bbb83c)
- ブロック [`00bbb83c`](#insn-00bbb83c) 範囲 `[['00bbb83c', '00bbb83f']]`
  - `FALL_THROUGH` [`00bbb83c`](#insn-00bbb83c) → [`00bbb840`](#insn-00bbb840)
- ブロック [`00bbb840`](#insn-00bbb840) 範囲 `[['00bbb840', '00bbb847']]`
  - `CONDITIONAL_JUMP` [`00bbb844`](#insn-00bbb844) → [`00bbb87c`](#insn-00bbb87c)
  - `FALL_THROUGH` [`00bbb844`](#insn-00bbb844) → [`00bbb848`](#insn-00bbb848)
- ブロック [`00bbb848`](#insn-00bbb848) 範囲 `[['00bbb848', '00bbb857']]`
  - `FALL_THROUGH` [`00bbb854`](#insn-00bbb854) → [`00bbb858`](#insn-00bbb858)
- ブロック [`00bbb858`](#insn-00bbb858) 範囲 `[['00bbb858', '00bbb85f']]`
  - `FALL_THROUGH` [`00bbb85c`](#insn-00bbb85c) → [`00bbb860`](#insn-00bbb860)
- ブロック [`00bbb860`](#insn-00bbb860) 範囲 `[['00bbb860', '00bbb863']]`
- ブロック [`00bbb864`](#insn-00bbb864) 範囲 `[['00bbb864', '00bbb87b']]`
- ブロック [`00bbb87c`](#insn-00bbb87c) 範囲 `[['00bbb87c', '00bbb887']]`
  - `CONDITIONAL_JUMP` [`00bbb884`](#insn-00bbb884) → [`00bbb860`](#insn-00bbb860)
  - `FALL_THROUGH` [`00bbb884`](#insn-00bbb884) → [`00bbb888`](#insn-00bbb888)
- ブロック [`00bbb888`](#insn-00bbb888) 範囲 `[['00bbb888', '00bbb88f']]`

## 命令位置別の参照

- [`00bbb810`](#insn-00bbb810) → [`00bbb824`](#insn-00bbb824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb828`](#insn-00bbb828) → [`00bbb864`](#insn-00bbb864) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb838`](#insn-00bbb838) → [`00bbb848`](#insn-00bbb848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb844`](#insn-00bbb844) → [`00bbb87c`](#insn-00bbb87c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb884`](#insn-00bbb884) → [`00bbb860`](#insn-00bbb860) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb810`](#insn-00bbb810)

~~~json
{
  "source": "00bbb810",
  "target": "00bbb824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb828`](#insn-00bbb828)

~~~json
{
  "source": "00bbb828",
  "target": "00bbb864",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb838`](#insn-00bbb838)

~~~json
{
  "source": "00bbb838",
  "target": "00bbb848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb844`](#insn-00bbb844)

~~~json
{
  "source": "00bbb844",
  "target": "00bbb87c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb884`](#insn-00bbb884)

~~~json
{
  "source": "00bbb884",
  "target": "00bbb860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
