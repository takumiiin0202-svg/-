/**
 * 共通スクリプト（たたき台）
 * 現時点ではモバイル用のナビゲーション開閉のみ。
 */
(function () {
  'use strict';

  var MOBILE_QUERY = '(max-width: 767px)';

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('global-nav');

  if (!toggle || !nav) {
    return;
  }

  var mql = window.matchMedia(MOBILE_QUERY);

  // 画面幅に応じて初期表示を切り替える。
  // PC幅ではCSSで常時表示するため hidden を外しておく。
  function syncNavState() {
    if (mql.matches) {
      nav.hidden = true;
      toggle.setAttribute('aria-expanded', 'false');
    } else {
      nav.hidden = false;
      toggle.setAttribute('aria-expanded', 'true');
    }
  }

  toggle.addEventListener('click', function () {
    var willOpen = nav.hidden;
    nav.hidden = !willOpen;
    toggle.setAttribute('aria-expanded', String(willOpen));
  });

  if (typeof mql.addEventListener === 'function') {
    mql.addEventListener('change', syncNavState);
  } else if (typeof mql.addListener === 'function') {
    mql.addListener(syncNavState);
  }

  syncNavState();
})();
